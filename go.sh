
#!/bin/bash

while :
do
	while :
	do
		
		read -n1 -r -p "Press space to continue..." key
		if [[ $key = "" ]]
		then
			break
		fi
	done

	echo starting
	while :
	do
		gst-launch-1.0 nvcamerasrc num-buffers=1 ! 'video/x-raw(memory:NVMM), width=(int)1280, height=(int)720,format=(string)I420' ! nvvidconv ! videoflip method=3 ! jpegenc ! filesink location='image.jpg'

		echo captured
		python camera.py
		read -n1 -r -p "Press r if you want to retake, otherwise press space" key
		if [[ $key = "" ]]
		then
			break
		
		else [[ $key = "r" ]]

			echo recapturing
		fi
	done
	
	
	python working.py --mode=visualization #--cluster_spec=clusterDefinition.py

	#echo opening
	#xdg-open output.jpg
done
