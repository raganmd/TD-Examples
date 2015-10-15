uri = {
	"10.0.0.2" : {
		"name" : "mission_control" ,
		"role" : "controller" ,
		"displays" : [
			"control01" 
		]
	},
	"10.0.0.3" : {
		"name" : "eyes" ,
		"role" : "node" ,
		"displays" : [
			"projector01" , 
			"projector02" 
		]
	}
}

displays = {
	"control01" : {
		"width" : 1920 ,
		"height" : 1080 ,
		"orientation" : 0
	},
	"projector01" : {
		"width" : 1920 ,
		"height" : 1080 ,
		"orientation" : 0
	},
	"projector02" : {
		"width" : 1920 ,
		"height" : 1080 ,
		"orientation" : 1
	}
}