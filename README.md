## Predicting high school dropout on Rio de Janeiro

This project aims to identify dropout risk students with public data from the Scholar Census [1] of 2016 and 2017.

School dropout is one of the main educational challenges in Brazil and has its peak in the transition from elementary to high school. According to a study by Insper [2], one in every 4 young people aged 15 to 17 interrupt their studies at this stage. Several dropout recovery programs have emerged in recent years in different states and municipalities, focusing on ac- tively seeking out-of-school youth. The aim of this work is to explore models for predicting this phenomenon in the universe of students from the 1st year of the state high schools in Rio de Janeiro with data from the School Census, aggregated to schools and favelas geolocation. To contemplate the grouping structure of students in schools, multilevel regression and random forest models were tested, and their performances compared in the surveyed data.

[1] Available at: http://portal.inep.gov.br/censo-escolar
[2] Available at: http://gesta.org.br/wp-content/uploads/2017/09/Politicas-Publicas-para-reducao-do-abandono-e-evasao-escolar-de-jovens.pdf


### Project Organization

    ├── LICENSE
    ├── README.md                  <- The top-level README for developers using this project (also know as this file!)
    ├── data
    │   ├── output                 <- Output processed data
    │   ├── treated                <- The cleaned and treated data for analysis
    │   └── raw                    <- The original, immutable data dump
    ├── notebooks                  <- Jupyter notebooks w/ data preprocessing and analysis
    ├── scripts                    <- R scripts w/ logit models
    ├── requirements.txt           <- Packages used in the code

#### Prerequisites

You need to have the packages on `requirements.txt` installed. To do that, open the terminal and run:

```
pip3 install -U -r requirements.txt
```

### Authors

* **Fernanda Scovino** - *Code maker* - [@fernandascovino](https://github.com/fernandascovino)

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

### Acknowledgments

* This README was adapted from [*A template to make good README.md*](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* The structure of this repository was adapted from [*Fast Project Templates*](https://github.com/JoaoCarabetta/project-templates)