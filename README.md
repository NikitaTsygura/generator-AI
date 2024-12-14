# template_django
template for djando start project.


1. Обрати розміщення для проєкту (тека- папка (директорії))
    
    `D:` - перейти на обраний диск.

    `cd <розьіщення/нізва теки>` - зайти до дерикторії.

    `cd..` - вийті до попередньої директорії

    `dir` - показати вміст поточної теки


2. Створити теку
    ```bash
   md 'Назва_теки'
   ```
3. Клонувати
    ```bash
    git clone "https://github.com/NikitaTsygura/template_django.git"
    ```

4. Віртуальне середовище 
- створити/підключити віртуальне середовице `.venv` підключити існуюче
    ```bash
  # створення віртуального середовища
    python -m venv .venv
    ```
- Активація віртуально середовища
```bash
# Windows
.venv\Scripts\activate
```
```bash
#Linux & MacOS
.venv\bin\activate
```

5. Встановлення необхідних модулей
```bash
pip istall requests.txt
```
<hr>
6. Створення нового проєкту Django