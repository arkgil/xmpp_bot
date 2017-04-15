start:
	docker start mongooseim

stop:
	docker stop mongooseim

setup:
	docker run -d -t -h mongooseim --name mongooseim  -p 5222:5222 \
	 -v `pwd`/mongooseim:/member mongooseim/mongooseim
