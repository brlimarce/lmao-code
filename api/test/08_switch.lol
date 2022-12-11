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

  I HAS A prod ITZ 0

	choice
	WTF?
		OMG 1
			VISIBLE "Enter birth year: "
			GIMMEH input
			VISIBLE DIFF OF 2022 AN input
			GTFO
		OMG 2
			VISIBLE "Enter bill cost: "
			GIMMEH input

      BTW Not supported
			BTW VISIBLE "Tip: " PRODUCKT OF input AN 0.1

      prod R PRODUKT OF input AN 0.1
      VISIBLE "Tip: " prod
			GTFO
		OMG 3
			VISIBLE "Enter width: "
			GIMMEH input

      BTW Not supported
			BTW VISIBLE "Square Area: " PRODUCKT OF input AN input
      
      prod R PRODUKT OF input AN input
      VISIBLE "Square Area: " prod
			GTFO
		OMG 0
			VISIBLE "Goodbye"
		OMGWTF
			VISIBLE "Invalid Input!"
	OIC

KTHXBYE
