var express = require('express');
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var Strip = require("./Strip");
net = require("net");
app.use(express.static('.'));
app.get('/', function(req, res) {
	res.sendfile('index.html');
});

app.get("/editor", function(req, res) {
	res.sendfile("editor.html")
});
var soc;


var strips = [];
io.on('connection', function(socket) {
	console.log('a user connected');
	soc = socket;

	socket.on('setPaused', function(data) {
		var id = data[0];
		data = data.slice(1, data.length);
		var seg = data[0];
		data = data.slice(1, data.length);
		if (data === "true") {
			strips[id].sendCommand("3", "" + seg + 1, function() {});
		} else {
			strips[id].sendCommand("3", "" + seg + 0, function() {});
		}
	});

	socket.on("getScripts", function(id) {
		if (strips[parseInt(id)] == undefined) {
			console.log("undefined")
			return;
		}
		strips[parseInt(id)].sendCommand("2", "", function(data) {
			socket.emit("scripts", data);
		})


	});

	socket.on("changeSegment", function(data) {
		strips[parseInt(data[0])].sendCommand("9", "" + data.slice(1, data.length), function() {})
	});

	socket.on("loadData", function(id) {
		var object = {};
		strips[id].sendCommand("7", "", function(data) {
			var segments = {};
			var segs = data.split(":");
			segs = segs.splice(0, segs.length - 1);
			for (var i = 0; i < segs.length; i++) {
				segments[i] = {};
				var items = segs[i].split(",");
				segments[i].id = items[0];
				segments[i].paused = items[1];
				segments[i].start = items[2];
				segments[i].end = items[3];
				segments[i].name = items[4];
				segments[i].script = items[5];
			}
			object["segments"] = segments;
			socket.emit("loadedData", JSON.stringify(object));
		});
	});

	socket.on("uploadFile", function(data) {
		strips[0].sendCommand("0", data, function(d) {
			console.log(d)
		})
	});

	socket.on("getCurrent", function(data) {
		var seg = data[0];
		var segments = []
		var current = [];
		strips[parseInt(seg)].sendCommand("7", "", function(data) {
			var segs = data.split(":");
			segs = segs.splice(0, segs.length - 1);
			for (var i = 0; i < segs.length; i++) {
				segments[i] = {};
				var items = segs[i].split(",");
				segments[i].id = items[0];
				segments[i].script = items[5];
			}
			socket.emit("getCurrentReturn", JSON.stringify(segments));
		});



	});

	socket.on("setScript", function(data) {
		var seg = data[0];
		data = data.slice(1, data.length);
		strips[parseInt(seg)].sendCommand("1", "" + data, function(d) {

		});
	});

	socket.on("getOptions", function(data) {
		var seg = data[0];
		data = data.slice(1, data.length);
		strips[parseInt(seg)].sendCommand("12", data, function(data) {
			socket.emit("getOptionsReturn", data);
		});
	});

	socket.on("setOptions", function(data) {
		var seg = data[0];
		data = data.slice(1, data.length);
		strips[parseInt(seg)].sendCommand("11", JSON.parse(data), function(data) {

		})
	});

	socket.on("command", function(data) {
		sendCommand(data);
	});

	socket.on("addSegment", function(data) {
		strips[parseInt(data[0])].sendCommand("8", "" + data.slice(1, data.length), function() {});
	});
	socket.on("removeSegment", function(data) {
		strips[parseInt(data[0])].sendCommand("10", "" + data.slice(1, data.length), function() {});
	});

	socket.on("ispaused", function(data) {
		if (strips[parseInt(data[0])] == undefined) {
			console.log("undefined")
			return;
		}
		strips[parseInt(data[0])].sendCommand("4", "" + data.slice(1, data.length), function(d2) {
			socket.emit("ispausedreturn", data.slice(1, data.length) + d2);
		});
	});
	socket.on("findStrips", function(data) {

		var finished = 0;
		for (var i = 0; i < 255; i++) {
			(function(l) {
				var temp = net.connect(13373, "192.168.1." + l);
				temp.setTimeout(100);
				temp.on("error", function(err) {
					finished++;
					if (finished >= 255) {
						//after()
					}
				});

				temp.on("connect", function(con) {
					console.log("Connected to Strip! " + l);
					var found = false;
					for (var a = 0; a < strips.length; a++) {
						if (strips[a].ip === l) {
							console.log("already have it. skipping..");
							found = true;
						}
					}
					if (!found) {
						strips.push(new Strip(temp, l));
						after();
					} else {
						after()
					}
					finished++;
					if (finished >= 255) {
						//after()
					}
				})
			}(i));
		}

		function after() {
			for (var i = 0; i < strips.length; i++) {
				(function(id) {
					strips[id].sendCommand("6", "", function(data) {
						data = data.split(",");
						strips[id].nam = data[0]
						strips[id].versio = data[1];
						socket.emit("stripInfo", id + "," + data[0] + "," + data[1]);
					});
				})(i);
			}
		}
	});

	socket.on('disconnect', function(data) {
		console.log("Disconnect user")

	});


});


//console.log(io)
http.listen(3000, function() {
	console.log('listening on *:3000');
});