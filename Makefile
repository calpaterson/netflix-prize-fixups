default: qualifying.csv probe.csv movie-titles.csv training-set.csv

.INTERMEDIATE: training-set.tar

qualifying.csv: nf_prize_dataset.tar.gz fixup-qualifying.py
	tar xfO $< download/qualifying.txt | ./fixup-qualifying.py > $@

probe.csv: nf_prize_dataset.tar.gz fixup-probe.py
	tar xfO $< download/probe.txt | ./fixup-probe.py > $@

movie-titles.csv: nf_prize_dataset.tar.gz fixup-movie-titles.py
	tar xfO $< download/movie_titles.txt | ./fixup-movie-titles.py > $@

training-set.csv: training-set.tar
	./fixup-training-set.py $< > $@

training-set.tar: nf_prize_dataset.tar.gz
	tar xfO $< download/training_set.tar > $@
