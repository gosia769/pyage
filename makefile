PYTHON = python

POINTS = points.csv
POINTS_GENERATOR = additional/generatePoints.py

$(POINTS):
	$(PYTHON) $(POINTS_GENERATOR) --points 50

run: $(POINTS)
	$(PYTHON) -m pyage.core.bootstrap pyage.tsp.tsp_conf INFO False 0.01 random $(POINTS)


run_tests: $(POINTS)
	$(PYTHON) ./additional/run_tests.py

clean:
	rm -f $(POINTS) *.log
