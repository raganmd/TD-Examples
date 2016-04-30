uri = { 
	"172.16.12.1211" : {
		"local_ID" : "asteroid" , 
		"media_path" : "c:\\" , 
		"role" : "calibrator" ,
		"tox" : "container_output/container_calibrator/container_calibrator.tox" ,
		"group" : { 
			"master_control" : [ 
				"control_display01"
			]
		} 
	} ,
	"172.16.12.1211" : {
		"local_ID" : "asteroid" , 
		"media_path" : "d:\\" , 
		"role" : "controller" ,
		"tox" : "container_output/container_controller/container_controller.tox" , 
		"group" : { 
			"master_control" : [ 
				"control_display01"
			]
		} 
	} ,
	"172.16.12.1211" : {
		"local_ID" : "asteroid" , 
		"media_path" : "e:\\" , 
		"role" : "node" ,
		"tox" : "container_output/container_node/container_node.tox" ,
		"group" : { 
			"west" : [
				"projector001" ,
				"projector002"   
			],
			"north" : [
				"projector003"
			]
		}
	},
	"172.16.12.114" : {
		"local_ID" : "walkabout" , 
		"media_path" : "c:\\" , 
		"role" : "calibrator" ,
		"tox" : "container_output/container_calibrator/container_calibrator.tox" ,
		"group" : { 
			"master_control" : [ 
				"control_display01"
			]
		} 
	} ,
	"172.16.12.1114" : {
		"local_ID" : "walkabout" , 
		"media_path" : "d:\\" , 
		"role" : "controller" ,
		"tox" : "container_output/container_controller/container_controller.tox" , 
		"group" : { 
			"master_control" : [ 
				"control_display01"
			]
		} 
	} ,
	"172.16.12.1114" : {
		"local_ID" : "walkabout" , 
		"media_path" : "e:\\" , 
		"role" : "node" ,
		"tox" : "container_output/container_node/container_node.tox" ,
		"group" : { 
			"west" : [
				"projector001" ,
				"projector002"   
			],
			"north" : [
				"projector003"
			]
		}
	},
	"172.16.12.112" : {
		"local_ID" : "snapdragon" , 
		"media_path" : "c:\\" , 
		"role" : "calibrator" ,
		"tox" : "container_output/container_calibrator/container_calibrator.tox" ,
		"group" : { 
			"master_control" : [ 
				"control_display01"
			]
		} 
	} ,
	"172.16.12.1121" : {
		"local_ID" : "snapdragon" , 
		"media_path" : "d:\\" , 
		"role" : "controller" ,
		"tox" : "container_output/container_controller/container_controller.tox" , 
		"group" : { 
			"master_control" : [ 
				"control_display01"
			]
		} 
	} ,
	"172.16.12.1121" : {
		"local_ID" : "snapdragon" , 
		"media_path" : "e:\\" , 
		"role" : "node" ,
		"tox" : "container_output/container_node/container_node.tox" ,
		"group" : { 
			"west" : [
				"projector001" ,
				"projector002"   
			],
			"north" : [
				"projector003"
			]
		}
	}
}