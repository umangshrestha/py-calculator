# PyCalculator
![plot](./docs/img.png)

This is real time interactive calulator. Implemented using  PyQt5.
* It will do basic arthemetic operation like add(+), subtract(-), division(/) and multiplicaiton(*), as well as power(^).
* Values are shown automatically in the display as input is being pressed.
* for division by 0, it will show <b>inf</b>.
* for error in calulation like +1+/2, it will display <b>nan</b>.


---
To run the application:

`$ python src/GUI.py`

To compile an application:

`$ pyinstaller  --onefile --windowed src/GUI.py` 
`$ ./dist/GUI`
___


For logic for creating calculator refer here: 
https://umangshrestha09.medium.com/introduction-to-creating-interpreter-using-python-c2a9a6820aa0


