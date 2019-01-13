# python-zip-extractor
This simple script allows you to extract all .zip file in a folder

## Installing

```
git clone https://github.com/lucadivit/python-zip-extractor

cd python-zip-extractor
```

## Usage

Example of usage:

First example: Extract all .zip files with password pwd1, pwd and  all .zip files without password in the folder Pcaps

```
python unzipFile.py --path=./Pcaps/ --password=pwd1,pwd2
```

Second example: Extract all .zip files without password and save them in Unzipped folder
```
python unzipFile.py --path=./Zip/ --folder=Unzipped
```

For help type:

```
python unzipFile.py --help
```

## Other

Type:
```
python unzipFile.py --help
```
to read flags and limitations.

## License

python-zip-extractor is licensed under ISC
