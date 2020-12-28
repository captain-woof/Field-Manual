# UI Redressing Steps

1. Add a div (id=outerDiv) that will contain the target iframe. Style:

	```
		#outerDiv {
			position: relative;
			overflow: hidden;
			z-index:1;
			top: ADJUST ACCORDINGLY; /* Position where you want to put */
			left: ADJUST ACCORDINGLY; /* the whole thing on the page */
		}
	```
2. Add an iframe (id=targetiframe) inside the div that points to target website. Style:
	```
		#targetiframe {
			position: absolute;
			z-index:2;
			opacity:0.01;
			top: -SOMETHING; /* Position so that target's button */
			left: -SOMETHING; /* goes to toppest left of parent div */
		}
	```
3. Test and adjust.

	
	

