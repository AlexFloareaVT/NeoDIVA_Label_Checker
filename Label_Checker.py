import os
import sys

# --- Phoneme Definitions ---

# Global phonemes shared across all languages
GLOBAL_PHONEMES = {
    'AP', 'SP', 'q', 'vf', 'trash', 'vtrash', 'ctrash', 'cl'
}

# Phonemes separated by language
ALL_PHONEMES = {
    'EN': {
        'ay', 'ae', 'aa', 'ah', 'aw', 'ao', 'ax', 'iy', 'ih', 'uw', 'uh',
        'eh', 'ey', 'er', 'ow', 'oy', 'oh', 'ch', 'b', 'd', 'dh', 'dr',
        'dx', 'el', 'em', 'en', 'f', 'g', 'hh', 'jh', 'k', 'l', 'n', 'nn', 'ng',
        'p', 'r', 's', 'sh', 't', 'th', 'tr', 'v', 'w', 'y', 'z', 'zh', 'm'
    },
    'ES': {
        'N', 'a', 'b', 'ch', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'r', 'rr', 's', 'sh', 't', 'ts', 'u', 'uu',
        'v', 'w', 'y', 'z', 'D', 'T', 'B', 'G', 'Y', 'x', 'ng', 'gn', 'th'
    },
    'FR': {
        'ae', 'ah', 'ax', 'b', 'ch', 'd', 'dx', 'ee', 'eh', 'en', 'f', 'g',
        'h', 'ih', 'in', 'j', 'k', 'l', 'm', 'n', 'ng', 'oe', 'oh', 'on',
        'oo', 'ou', 'p', 'r', 'rh', 'rx', 's', 'sh', 't', 'uh', 'un',
        'uy', 'v', 'w', 'y', 'z'
    },
    # --- NEW LANGUAGE ADDED ---
    'HY': {
        'a', 'ax', 'b', 'ch', 'd', 'dx', 'dz', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'k\'', 'l', 'm', 'n', 'ng', 'o', 'p', 'p\'', 'r', 'rr', 's', 'sh',
        't', 't\'', 'ts', 'u', 'v', 'w', 'x', 'y', 'z', 'zh'
    },
    # --- END OF NEW LANGUAGE ---
    'IT': {
        'Y', 'N', 'a', 'b', 'ch', 'd', 'dz', 'e', 'ee', 'f', 'g', 'gl',
        'gn', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'oo', 'p', 'q', 'r',
        'rr', 's', 'sh', 't', 'ts', 'u', 'uu', 'v', 'w', 'y', 'z'
    },
    'JA': {
        'a', 'i', 'A', 'I', 'O', 'U', 'E', 'u', 'e', 'o', 'N', 'w', 'r',
        'ch', 't', 'ts', 'y', 'p', 's', 'sh', 'd', 'f', 'g', 'h', 'j',
        'k', 'z', 'v', 'b', 'n', 'm', 'dy', 'my', 'py', 'gy', 'by', 'hy',
        'ky', 'ny', 'ry', 'ty', 'fy', 'dz', 'vy', 'zy', 'l'
    },
    'KA': {
        'G', 'a', 'b', 'ch', 'ch-', 'd', 'dz', 'e', 'g', 'hh', 'i', 'j',
        'k-', 'kh', 'l', 'm', 'n', 'o', 'p-', 'ph', 'q-', 'r', 's', 'sh',
        't', 't\'', 'ts', 'ts-', 'u', 'v', 'w', 'x', 'y', 'z', 'zh', 'rr'
    },
    'KO': {
        'K', 'L', 'M', 'N', 'NG', 'P', 'RR', 'T', 'a', 'b', 'ch', 'd', 'e',
        'eo', 'eu', 'f', 'g', 'h', 'i', 'j', 'jj', 'k', 'kk', 'l', 'm',
        'n', 'o', 'p', 'pp', 'r', 's', 'ss', 't', 'th', 'tt', 'u', 'v',
        'w', 'y', 'z'
    },
    'PL': {
        'A', 'C', 'E', 'H', 'J', 'L', 'N', 'O', 'S', 'X', 'Z', 'a', 'b',
        'c', 'cz', 'ch', 'd', 'dX', 'dZ', 'dz', 'e', 'f', 'g', 'h', 'hh',
        'i', 'j', 'jh', 'k', 'l', 'm', 'n', 'ng', 'nn', 'o', 'p', 'r',
        's', 'sz', 'sh', 't', 'u', 'w', 'y', 'z'
    },
    'PT': {
        'a', 'ae', 'an', 'ax', 'b', 'ch', 'd', 'dj', 'e', 'eh', 'en', 'f',
        'g', 'h', 'hr', 'i', 'i0', 'in', 'j', 'k', 'l', 'lh', 'm', 'n',
        'ng', 'nh', 'o', 'oh', 'on', 'p', 'r', 'rh', 'rr', 'rw', 's',
        'sh', 't', 'u', 'u0', 'un', 'v', 'w', 'x', 'y', 'z'
    },
    'RO': {
        'a', 'ax', 'b', 'ch', 'cl', 'd', 'dg', 'e', 'ea', 'eo', 'f', 'g',
        'h', 'i', 'ij', 'j', 'k', 'l', 'm', 'n', 'ng', 'o', 'oa', 'p',
        'r', 'rr', 's', 'sh', 't', 'ts', 'u', 'ux', 'v', 'w', 'y', 'z'
    },
    'RU': {
        'A', 'E', 'Y', 'a', 'b', 'bj', 'c', 'ch', 'd', 'dj', 'e', 'f',
        'fj', 'g', 'gj', 'h', 'hh', 'hj', 'i', 'j', 'k', 'kj', 'l', 'lj',
        'm', 'mj', 'n', 'nj', 'o', 'p', 'pj', 'r', 'rj', 's', 'sh',
        'shj', 'sj', 't', 'tj', 'u', 'v', 'vj', 'y', 'z', 'zh', 'zj'
    },
    'TH': {
        'A', 'B', 'D', 'E', 'I', 'K', 'O', 'U', 'Ua', 'W', 'Y', 'a', 'au',
        'b', 'ch', 'd', 'e', 'f', 'h', 'i', 'ia', 'j', 'k', 'kk', 'l',
        'L', 'm', 'n', 'ng', 'o', 'p', 'pp', 'r', 's', 't', 'tt', 'u',
        'ua', 'v', 'w', 'y', 'z', 'N', 'gn'
    },
    'ZH': {
        'E', 'I', 'N', 'U', 'a', 'ai', 'ao', 'b', 'c', 'ch', 'd', 'e',
        'ei', 'er', 'f', 'g', 'h', 'i', 'iE', 'ia', 'io', 'ir', 'iz',
        'j', 'k', 'l', 'm', 'n', 'ng', 'o', 'ou', 'p', 'q', 'r', 's',
        'sh', 't', 'u', 'uE', 'ua', 'ue', 'uo', 'v', 'vE', 'w', 'x',
        'y', 'z', 'zh'
    }
}

# --- Helper Functions ---

def get_lang_from_dirname(dirpath):
    """
    Extracts the language code (e.g., 'EN') from a folder name (e.g., 'Alex_en').
    Returns None if no valid language tag is found.
    """
    folder_name = os.path.basename(dirpath)
    parts = folder_name.split('_')
    if len(parts) > 1:
        lang_tag = parts[-1].upper()
        if lang_tag in ALL_PHONEMES:
            return lang_tag
    return None

def validate_phoneme(phoneme, lang_code, lang_phoneme_set):
    """
    Validates a single phoneme.
    Returns an error message string if invalid, or None if valid.
    """
    # 1. Check suggestion phonemes ('pau', 'br')
    if phoneme == 'pau':
        return "SUGGESTION: 'pau' found. These phonemes aren't wrong, but should be named SP for pau."
    if phoneme == 'br':
        return "SUGGESTION: 'br' found. These phonemes aren't wrong, but should be named AP for br."

    # 2. Check global phonemes
    if phoneme in GLOBAL_PHONEMES:
        return None  # Valid

    # 3. Check for language-tagged phonemes (e.g., 'ja/a')
    if '/' in phoneme:
        try:
            tag_lang, phone_to_check = phoneme.split('/', 1)
            tag_lang = tag_lang.upper()
            
            if tag_lang in ALL_PHONEMES:
                # Check if the phoneme exists in its own language set or globals
                if (phone_to_check in ALL_PHONEMES[tag_lang] or 
                    phone_to_check in GLOBAL_PHONEMES):
                    return None  # Valid tagged phoneme
                else:
                    return f"TYPO: Tagged phoneme '{phone_to_check}' not found in language set '{tag_lang}'."
            else:
                return f"ERROR: Unknown language tag '{tag_lang}' in phoneme '{phoneme}'."
        except ValueError:
            return f"ERROR: Malformed language-tagged phoneme '{phoneme}'."

    # 4. Check against the folder's language-specific set
    if phoneme in lang_phoneme_set:
        return None  # Valid

    # 5. If all checks fail, it's a typo
    return f"TYPO: Phoneme not found in global list or '{lang_code}' language list."

def process_folder(dirpath, lab_files, lang_code, root_path):
    """
    Processes all .lab files in a given folder and generates a log file.
    """
    # Get relative path for privacy in console output
    relative_dirpath = os.path.relpath(dirpath, root_path)
    print(f"--- Processing folder: {relative_dirpath} (Language: {lang_code}) ---")
    log_entries = []
    lang_phoneme_set = ALL_PHONEMES[lang_code]

    for lab_file in lab_files:
        file_path = os.path.join(dirpath, lab_file)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception as e:
            # log_file is just the filename, which is fine for privacy
            log_entries.append(f"CRITICAL ERROR: Could not read file {lab_file}. Reason: {e}\n")
            continue

        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            if not line:
                continue  # Skip empty lines

            parts = line.split()
            
            # Expecting format: start_time end_time phoneme
            if len(parts) < 3:
                log_entries.append(f"WARNING: Malformed line in {lab_file} (Line {line_num}): '{line}'\n")
                continue
            
            phoneme = parts[2]
            
            # Validate the phoneme
            error_message = validate_phoneme(phoneme, lang_code, lang_phoneme_set)
            
            if error_message:
                log_entries.append(f"Issue in {lab_file} (Line {line_num}): Phoneme '{phoneme}' -> {error_message}\n")

    # --- MODIFIED SECTION ---
    # Always create a log file for this folder
    folder_name = os.path.basename(dirpath)
    log_file_name = f"{folder_name}_errors.log"
    # Save the log in the root folder, not the subfolder
    log_file_path = os.path.join(root_path, log_file_name)
    
    # Get relative path for log file output (for privacy)
    relative_log_path = os.path.relpath(log_file_path, root_path)
    
    try:
        with open(log_file_path, 'w', encoding='utf-8') as log_f:
            # Use relative_dirpath (defined at start of function) for privacy
            log_f.write(f"Error Log for folder: {relative_dirpath}\n")
            log_f.write(f"Detected Language: {lang_code}\n")
            log_f.write("=" * 30 + "\n\n")
            
            if log_entries:
                # If there are errors, write them
                log_f.writelines(log_entries)
                # Use relative_log_path for privacy
                print(f"!!! Issues found. Log file created at: {relative_log_path}\n")
            else:
                # If there are no errors, write "No errors found"
                log_f.write("No errors found.\n")
                # Use relative_log_path for privacy
                print(f">>> No issues found. Log file created at: {relative_log_path}\n")
                
    except Exception as e:
        # Use relative_log_path for privacy and fix typo (was 'log_file_route')
        print(f"CRITICAL ERROR: Could not write log file {relative_log_path}. Reason: {e}\n")
    # --- END OF MODIFIED SECTION ---


# --- Main Execution ---

def main():
    """
    Main function to drive the script.
    """
    # 1. Get root folder path from user
    root_folder_path = input("Please enter the path to the root folder to scan: ").strip()

    if not os.path.isdir(root_folder_path):
        print(f"Error: The path '{root_folder_path}' is not a valid directory.")
        print("Please run the script again.")
        sys.exit(1)

    # Use the user-provided path as-is, since they just typed it.
    # All *subsequent* paths will be relative to this.
    print(f"\nScanning all subfolders starting from: {root_folder_path}\n")

    # 2. Crawl through all subfolders
    for dirpath, dirnames, filenames in os.walk(root_folder_path, topdown=True):
        
        # 3. Check if the *current* folder has a valid language tag
        lang_code = get_lang_from_dirname(dirpath)
        
        if lang_code:
            # 4. Check if this folder contains any .lab files
            lab_files = [f for f in filenames if f.endswith('.lab')]
            
            if lab_files:
                # 5. Process this folder
                process_folder(dirpath, lab_files, lang_code, root_folder_path)
                
                # Optional: Prevent os.walk from going *deeper* into this
                # folder, as we assume .lab files are not nested further
                # within a language folder.
                # dirnames.clear() 
            
    print("Scan complete.")

if __name__ == "__main__":
    main()
