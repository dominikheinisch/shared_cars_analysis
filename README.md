# shared-cars analysis

## 1. requirements

- python >= 3.6
- `pip3 install -r requirements.txt`

## 2. running jupyter-lab

```
jupyter-lab
```

## 2. sample data analysis

- using `jupyter-lab`
    - read and run `shared_cars.ipynb`

## 3. working on full data

- download data https://www.kaggle.com/gidutz/autotel-shared-car-locations?select=2020_02_25.csv
- save data to `'/datasets'`
- using `jupyter-lab`
    - read and run `full_data.ipynb`

## 4. testing

loader and input data validation / testing

### 4.1 requirements
 - `pip3 install -r test_requirements.txt`

### 4.2 run
```
python3 -m pytest -vs
```