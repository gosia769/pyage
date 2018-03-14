PYTHON = python

POINTS = points.csv
POINTS_GENERATOR = additional/generatePoints.py

OUT_DIR = out

$(POINTS):
	$(PYTHON) $(POINTS_GENERATOR) --points 50

$(OUT_DIR):
	mkdir out

run: $(POINTS) $(OUT_DIR)
	$(PYTHON) -m pyage.core.bootstrap pyage.tsp.tsp_conf INFO False 0.01 random $(POINTS)

run_tests: $(POINTS) $(OUT_DIR)
	$(PYTHON) ./additional/run_tests.py

clean:
	rm -f $(POINTS) *.log
	rm -Rf out
