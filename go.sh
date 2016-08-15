
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
		#720x480
		#
		#
		gst-launch-1.0 nvcamerasrc num-buffers=1 ! 'video/x-raw(memory:NVMM), width=(int)720, height=(int)480,format=(string)I420' ! nvvidconv ! videoflip method=3 ! jpegenc ! filesink location='image.jpg'

		echo captured
		echo "press any key to continue"
		python camera.py
		read -n1 -r -p "Press r if you want to retake, otherwise press space" key
		if [[ $key = "" ]]
		then
			echo -e \nSpace
			break
		else [[ $key = "r" ]]

			echo -e \n recapturing
		fi
	done
	python working.py --mode=visualization #--cluster_spec=clusterDefinition.py

	#echo opening
	#xdg-open output.jpg
done
