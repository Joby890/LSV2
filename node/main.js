$(document).ready(function() {
	$(".currentStrip").data("id", 0)
	var socket = io();



	$(".findStrips").on("click", function() {
		socket.emit("findStrips", " ");

		update();
	});



	socket.on("stripInfo", function(data) {
		data = data.split(",");
		var found = false;
		$(".allStrips").children().each(function(index) {
			if ($(this).data("id") == data[0]) {
				found = true;
				$(this).text(data[1] + " " + data[2]);
			}
		});
		if (!found) {
			var div = $('<div class="strip">' + data[1] + ' ' + data[2] + '</div>');
			div.data("id", data[0]);
			$(".allStrips").prepend(div);
		}
		$(".strip").on("click", function() {
			var id = $(this).data("id");
			$(".currentStrip").data("id", id);
			$(".currentStrip").slideUp(function() {
				socket.emit("loadData", id);
				$(".currentStrip").empty();
			});

		});
	});

	socket.on("loadedData", function(data) {
		var object = JSON.parse(data);

		var scripts = object.scripts;

		for (var seg in object.segments) {
			var div = $('<div class="segment"> <div class="segmentName">' + object.segments[seg].name + '</div><input class="changeName" type="text"></input><div class="segmentId">' + '</div>  <select class="currentScripts">  </select> <img class="flipStatus" src="/assests/play.png"></img><button class="setScript"> Set Script </button><button class="removeSegment"> Remove Segment </button><div><input class="changeStart" type="text"></input><input class="changeEnd" type="text"></input> <button class="changeSeg"> Change </button></div>  </div > ');
			$(".currentStrip").append(div);

			$(div).find(".segmentId").data("id", object.segments[seg].id);
			$(div).find(".changeStart").val(object.segments[seg].start)
			$(div).find(".changeEnd").val(object.segments[seg].end)
			$(div).find(".changeName").val(object.segments[seg].name)
			$(".currentScripts").empty();
			// var strings = scripts.split(",");
			// for (var i = 0; i < strings.length; i++) {
			// 	$(".currentScripts").append($("<option></option>").attr("value", strings[i]).text(strings[i]));
			// 	$(".currentScripts").attr("size", strings.length);
			// }
			update();
		}
		socket.emit("getScripts", getCurrentStrip());
		$(".changeName").hide();

		$(".removeSegment").on("click", function() {
			id = $(this).parent().find(".segmentId").data("id");
			socket.emit("removeSegment", getCurrentStrip() + id);
		});

		$(".segmentName").on("click", function() {
			$(this).parent().find(".changeName").show();
			//$(".changeName").hide();
			$(this).hide()
		});

		$(".segment").on("click", function(e) {
			if (e.target != this) {
				return;
			}
			namechange = $(this).find(".changeName");
			namechange.hide();
			segmentname = $(this).find(".segmentName");
			segmentname.text(namechange.val());
			segmentname.show();
		})

		$(".changeSeg").on("click", function() {
			id = $(this).parent().parent().find(".segmentId").data("id")
			name = $(this).parent().parent().find(".changeName").val();
			start = $(this).parent().find(".changeStart").val();
			end = $(this).parent().find(".changeEnd").val();
			socket.emit("changeSegment", getCurrentStrip() + id + "," + start + "," + end + "," + name);
			socket.emit("loadData", getCurrentStrip());
			$(".currentStrip").empty();
		});
		$(".currentStrip").append('<br><br><br><br><div class="addSegment"><input class="id" type="text"></input><input class="start" type="text"></input><input class="end" type="text"></input><button class="addSubmit">Add!</button> </div>')

		$(".currentStrip").slideDown();
		$(".setScript").on("click", function(e) {
			socket.emit("setScript", getCurrentStrip() + $(this).parent().find(".segmentId").data("id") + $(this).parent().find('.currentScripts :selected').text())


		});

		$(".addSubmit").on("click", function() {
			set = getCurrentStrip() + $(this).parent().find(".start").val() + "," + $(this).parent().find(".end").val() + "," + $(this).parent().find(".id").val();
			socket.emit("addSegment", set)

			socket.emit("loadData", getCurrentStrip());
			$(".currentStrip").empty();
		});


		$(".flipStatus").on("click", function() {
			if ($(this).attr("src") == "/assests/play.png") {
				socket.emit('setPaused', getCurrentStrip() + $(this).parent().find(".segmentId").data("id") + "false");
				$(this).attr("src", "/assests/pause.png");
			} else {
				socket.emit('setPaused', getCurrentStrip() + $(this).parent().find(".segmentId").data("id") + "true");
				$(this).attr("src", "/assests/play.png");
			}

			//update();

		});


	});

	socket.on("ispausedreturn", function(data) {
		var seg = data[0];
		var paused = data[1];
		$(".segment").each(function(index) {
			id = $(this).find(".segmentId").data("id");
			if (seg == id) {
				if (paused == 0) {
					$(this).find(".flipStatus").attr("src", "/assests/pause.png")
				} else {
					$(this).find(".flipStatus").attr("src", "/assests/play.png")
				}

			}
		});
	});

	socket.on("getCurrentReturn", function(data) {
		var object = JSON.parse(data);
		for (var a in object) {
			$(".segment").each(function(index) {
				id = $(this).find(".segmentId").data("id");
				if (object[a].id == id) {
					if ($(this).find(".currentScripts").val() !== object[a].script) {
						$(this).find(".currentScripts").val(object[a].script);
					}

				}
			});
		}
	});
	var self = this

	socket.on("scripts", function(data) {
		$(".currentScripts").empty();
		var strings = data.split(",");
		for (var i = 0; i < strings.length; i++) {
			$(".currentScripts").append($("<option></option>").attr("value", strings[i]).text(strings[i]));
			$(".currentScripts").attr("size", strings.length);

		}
		$(".currentScripts").on("dblclick", function() {
			string = $(this).val();
			socket.emit("getOptions", getCurrentStrip() + string);
			self.currentEditing = string;
		});
		//$(".currentScripts").text(data);
	});

	socket.on("getOptionsReturn", function(data) {
		$(".scriptEditor").empty();
		data.forEach(function(item) {
			div = $('<div class="Option"></div>');
			if (item.type == "colorpicker") {
				div.append('' + item.name + ' <input class="color"></input>');
				$(".color").colorPicker({
					renderCallback: function($elm, toggled) {
						updateOptions(data, item, self.currentEditing, this.color.colors.RND.rgb);
					}
				});
			}
			$(".scriptEditor").append(div)
		});
		$(".scriptEditor")
	});

	function updateOptions(options, option, name, rgb) {
		//option.value
		option.value = "" + rgb.r + "," + rgb.g + "," + rgb.b;
		newobject = {};
		newobject.name = name;
		newobject.options = options
		socket.emit("setOptions", getCurrentStrip() + JSON.stringify(newobject));
	}

	function getCurrentStrip() {
		return $(".currentStrip").data("id");
	}

	setInterval(function() {
		update()
	}, 5000)


	function update() {
		//Update Current Scripts
		//socket.emit("getScripts", getCurrentStrip());
		socket.emit("getCurrent", "" + getCurrentStrip());
		for (var i = 0; i < $(".segment").length; i++) {
			socket.emit("ispaused", getCurrentStrip() + i)
		}

	}


	//update();

});