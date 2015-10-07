function Strip(n, ip) {
	this.n = n;
	this.ip = ip;
	this.nam = "";
	this.versio = "";
	this.callbacks = {};

	Strip.prototype.sendCommand = function(pid, command, cb) {

		var callbackID = Math.floor((Math.random() * 4000) + 1);
		while (this.callbacks[callbackID] != undefined) {
			callbackID = Math.floor((Math.random() * 4000) + 1);
		}
		obj = {};
		obj.id = callbackID;
		obj.command = command;
		obj.pid = pid;
		stringy = JSON.stringify(obj);
		this.callbacks[callbackID] = cb;
		if (stringy.length >= 100) {
			this.n.write("0" + stringy.length)
		} else {
			this.n.write("00" + stringy.length)
		}

		this.n.write(stringy);

	}
	var self = this;
	this.n.on("data", function(data) {
		string = data.toString();
		string = replaceAll("} {", "},{", string)
		string = "[" + string + "]";
		object = JSON.parse(string);
		object.forEach(function(item) {
			self.callbacks[item.id](item.returnString)
		});

		// if (string.split(" {").length >= 1) {

		// 	split = string.split(" {");
		// 	console.log("Multiple return size is " + split.length)
		// 	split.forEach(function(item, index) {
		// 		item = "{" + item;
		// 		console.log(JSON.parse(item));
		// 	});

		// } else {
		// 	console.log("Size is 1")
		// 	object = JSON.parse(string);
		// 	console.log(object)
		// }

		// data = data.toString();
		// id = data.split(",")[0];
		// console.log(id)
		// data.replace(id, "");
		// self.callbacks[id](data.slice(1, data.length));
		//self.currentCB(data.toString());
	})
}

function replaceAll(find, replace, str) {
	return str.replace(new RegExp(find, 'g'), replace);
}


module.exports = Strip;