.PHONY: run clean

run: controller.py
	flask --app controller.py run

clean:
	rm mood_db.txt
	rm users.txt
	touch mood_db.txt
	touch users.txt
