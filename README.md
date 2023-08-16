# rst-URL-link-Checker

## Installation for Windows
```bash
git clone https://github.com/1taroh/rst-URL-link-Checker
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## How to use
Change `directory_path` where you want to check URL link in `main.py`.
Then,
```bash
python main.py
```
If you want to save the list, type `y`.
```bash
Do you want to save this list? y/n
n
```

## Example
The example files are included.
Example `directory_path` is `directory_path = "./test/rstfiles/source/"`.
```bash
python main.py
rst files are ..
--------------------------------------------------------------------------
['./test/rstfiles/source/1.rst',
 './test/rstfiles/source/index.rst',
 './test/rstfiles/source/source2\\2.rst']
--------------------------------------------------------------------------
The dataframe is ..
--------------------------------------------------------------------------
                               rst file              text  line                                                URL                                        http status
0          ./test/rstfiles/source/1.rst             yahoo     1                                 http://yahoo.co.jp                                                200      
1          ./test/rstfiles/source/1.rst  aaaaaaaaaaaa.com     3                          https://aaaaaaaaaaaa.com/  Error: HTTPSConnectionPool(host='aaaaaaaaaaaa....      
2          ./test/rstfiles/source/1.rst            1taroh     5  https://github.com/1taroh/rst-URL-link-Checkeraaa                                                404      
3      ./test/rstfiles/source/index.rst               CNN    13                                     http://cnn.com                                                200      
4      ./test/rstfiles/source/index.rst            google    15                                  http://google.com                                                200      
5  ./test/rstfiles/source/source2\2.rst           youtube     1                                 http://youtube.com                                                200      
--------------------------------------------------------------------------
Do you want to save this list? y/n
```

## 最後に
作ったはいいが，使わなかった...
必要な人には必要だと思われる