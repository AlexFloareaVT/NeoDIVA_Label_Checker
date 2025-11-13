# NeoDIVA Phoneme .lab File Checker

This Python script crawls a directory, finds subfolders containing `.lab` files, and validates the phonemes within them based on a language tag in the folder's name. This script uses all the phoneme sets included in the NeoDIVA DiffSinger model, but should be applicable to most datasets.

It checks for:
* **Typos:** Phonemes not found in the global list or the specified language's phoneme set. (AP, SP, vf, q, cl, ctrash, vtrash and trash)
* **Suggestions:** `pau` (suggests `SP`) and `br` (suggests `AP`).
* **Tagged Phonemes:** Validates phonemes with language tags (e.g., `ja/a`).

## 1. Supported Languages

The script recognizes folder names ending in the following language tags (case-insensitive):

* `_en` English (Arpasing+ Phoneme Set)
* `_es` Spanish (Namine Criss Phoneme Set)
* `_fr` French (Millefeuille Phoneme Set)
* `_it` Italian (Gianloop Phoneme Set)
* `_ja` Japanese (Standard Phoneme Set)
* `_ka` Georgian (Datawave Phoneme Set)
* `_ko` Korean (Team CODA Phoneme Set)
* `_pl` Polish (PixPrucer Phoneme Set)
* `_pt` Portuguese (Brazillian, Team BRAPA Phoneme Set)
* `_ro` Romanian (NeoDIVA Phoneme Set)
* `_ru` Russian (Lunai Phoneme Set)
* `_th` Thai (PrintMOV Phoneme Set)
* `_zh` Chinese (TGM Phoneme Set)

## 2. Save the Script

Save the Python file anywhere on your computer, ideally in documents in it's own folder for organization.

## 3. Prepare Your Folders

This is the most important step. The script is designed to find language codes in your folder names.

* A folder's name **must** end with an underscore (`_`) followed by one of the two-letter language codes listed above (e.g., `_en`, `_es`, `_ja`).
* The script will skip any folder that does not match this format.

### Correct Folder Naming Examples:
```
C:\My_Data\Speaker_01_en
C:\My_Data\Recordings_fr
C:\My_Data\Section_4\Speaker_10_ko
```

### Incorrect Folder Naming Examples:
* `C:\My_Data\English_Files` (The script will skip this folder because it has no language tag).
* `C:\My_Data\Speaker_pt_files` (The script will skip this because the `_pt` tag is not at the very end of the folder name).

All your `.lab` files should be placed directly inside these language-tagged folders.

## 4. Run the Script

1.  Open your terminal (like **Command Prompt**, **PowerShell**, or **Windows Terminal**).
2.  Use the `cd` command to move to the folder where you saved the `check_phonemes.py` file.

    ```bash
    # Example:
    cd C:\Users\Example\Documents\LabelChecker
    ```

3.  Once you are in the correct folder, run the script:

    ```bash
    python check_phonemes.py
    ```
    (You may need to use `py` instead of `python` depending on your setup).

## 5. Enter the Root Folder Path

1.  The script will ask you:
    ```
    Please enter the path to the root folder to scan:
    ```
2.  This is the main folder that *contains* all your language-tagged folders (like `C:\My_Data` from the example above).
3.  Copy the full path to this root folder, paste it into the terminal, and press **Enter**.

## 6. Check the Log Files

The script will scan all the subfolders.

* When it is finished, **look inside your root folder** (the path you just gave the script).
* For every language-tagged folder it processed (e.g., `Speaker_01_en`), it will create a new log file in that root directory (e.g., `Speaker_01_en_errors.log`).
* Open these `.log` files to see the results.
    * If any typos, suggestions (`pau`/`br`), or malformed lines were found, they will be listed with the file name and line number.
    * If a folder's labels were all correct, its log file will simply say "No errors found."
