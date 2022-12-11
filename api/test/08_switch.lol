OBTW
  Status: NOT WORKING
  Remark/s: IT should support variables.
TLDR
HAI

	I HAS A choice
	I HAS A input

	BTW if w/o MEBBE, 1 only, everything else is invalid
	VISIBLE "1. Compute age"
	VISIBLE "2. Compute tip"
	VISIBLE "3. Compute square area"
	VISIBLE "0. Exit"

	VISIBLE "Choice: "
	GIMMEH choice

  I HAS A diff ITZ 0
  I HAS A prod ITZ 0
  I HAS A sqarea ITZ 0

	BTW IT R choice
  choice
	WTF?
		OMG 1
			VISIBLE "Enter birth year: "
			GIMMEH input
			BTW VISIBLE DIFF OF 2022 AN input
      diff R DIFF OF 2022 AN input
      VISIBLE diff
			GTFO
		OMG 2
			VISIBLE "Enter bill cost: "
			GIMMEH input
			BTW VISIBLE "Tip: " PRODUCKT OF input AN 0.1
      prod R PRODUKT OF input AN 0.1
      VISIBLE prod
			GTFO
		OMG 3
			VISIBLE "Enter width: "
			GIMMEH input
			BTW VISIBLE "Square Area: " PRODUCKT OF input AN input
      sqarea R PRODUKT OF input AN input
      VISIBLE sqarea
			GTFO
		OMG 0
			VISIBLE "Goodbye"
		OMGWTF
			VISIBLE "Invalid Input!"
	OIC

KTHXBYE
