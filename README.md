# Blockchain at Berkeley
Repo for Blockchain at Berkeley courses

## Courses

| **Blockchain Development**                                                                                                                               | **Blockchain Fundamentals**                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [Lectures](https://www.youtube.com/playlist?list=PLSONl1AVlZNWJVixT2vwY9-6O7kgM4het)                                                                     | [Lectures](https://www.youtube.com/playlist?list=PLSONl1AVlZNXUhgIrfgI6E3ayShvKI-o6) |
| [Resources](https://blockchain.berkeley.edu/courses/spring-2021-developers-decal/)                                                                       | [Resources](https://blockchain.berkeley.edu/courses/spring-2021-fundamentals-decal/) |
| [Repository [2021]](https://github.com/BerkeleyBlockchain/dev-decal-sp21) <br/>[Repository [2020]](https://github.com/BerkeleyBlockchain/dev-decal-sp20) |                                                                                      |

## Workload

Expected pace is 2 Fundamentals Lectures and 1 Dev Lecture per week. However, only the very next lecture can be watched without finishing Problem Set of the previous one (relevant only for Dev course). Dev Lectures weeks can be replaced with Problem Set weeks if necessary. Goal is to finish the course by the end of Feb, 2022.

| Week                   | Fundamentals Lectures | Dev Lectures | Problem Sets | Notes                                                                                                                                                                                          |
|------------------------|-----------------------|--------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1) 22.11.21 - 28.11.21 | 1, 2, 3               | 1            | -            | First PS will really benefit from covering Fundamentals Lectures 1-6. So, we will replace the PS and Dev Lecture 2 with additional Fundamentals Lecture to cover all needed material by week 3 |
| 2) 29.11.21 - 5.12.21  | 4, 5, 6               | -            | -            |                                                                                                                                                                                                |
| 3) 6.12.21 - 12.12.21  | -                     | -            | 1            | Week dedicated to PS 1                                                                                                                                                                         |
| 4) 13.12.21 - 19.12.21 | 7                     | 2            | 1            | Finish PS 1 and continue with the lectures                                                                                                                                                     |
| 5)                     |                       |              |              |                                                                                                                                                                                                |

## Misc

* [Modern Blockchain Development series from Near](https://www.youtube.com/playlist?list=PL9tzQn_TEuFWweVbfTbaedFdwVrvaYPq4)
* [Blockchain and Money Course from MIT](https://www.youtube.com/playlist?list=PLUl4u3cNGP63UUkfL0onkxF6MYgVa04Fn)
* [Solidity YouTube Tutorial](https://www.youtube.com/playlist?list=PL16WqdAj66SCOdL6XIFbke-XQg2GW_Avg) (bit outdated but really well-delivered)


## Development

1. Create a virtual environment
```shell
python -m venv venv
source venv/bin/activate
```
2. Install project dependencies
 ```shell
make install
```
4. Configure pre-commit
```shell
pre-commit install
```
4. Run linters
```shell
make lint
```
5. Fix style errors
```shell
make fix
```

### Style guides
- Flake8 rules: https://lintlyci.github.io/Flake8Rules/
- Solhint rules: https://protofire.github.io/solhint/docs/rules.html
- Commit messages (optional): https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716

### Requirements
1. Sync requirements (install missing packages, delete the redundant once, bump versions)
```shell
make sync-requirements
```
2. Compile requirements*.txt (required after changing requirements*.in)
```shell
make compile-requirements
```
