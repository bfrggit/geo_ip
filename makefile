DIRS     := 
PYC      := *.pyc

all:

.PHONY: clean
clean:
	-$(RM) -f $(PYC)
	-for d in $(DIRS); do \
		$(MAKE) --directory=$$d clean; \
	done
