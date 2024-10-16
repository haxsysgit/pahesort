# Animepahe File Organizer

## Description

This project is designed to help manage and organize the downloaded animepahe files. It includes functionalities to gather, rename, and organize anime files into appropriate folders based on their names and formats. The script handles files with specific naming conventions and organizes them into directories to make managing and locating anime episodes easier.

## Features

- **Gather Anime Files**: Moves files that start with "AnimePahe" into a dedicated directory.
- **Rename Anime Files**: Renames files to a standard format: `EpisodeNumber-AnimeName-Quality.ext`.
- **Organize Anime Files**: Moves files into folders named after the anime.

## Requirements

- Python 3.x
- Standard Python libraries: `os`, `shutil`, `re`, `argparse`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/haxsysgit/pahesort.git
   ```

2. Navigate into the project directory:
    ```bash
    cd pahesort
    ```

## Usage

### Command-Line Arguments

- `--path` or `-p`: Specify the path where the anime files are located.
- `--all` or `-a`: Perform all operations: gather, rename, and organize, Default is the Downloads directory.
- `--rename` or `-r`: Only rename the anime files.
- `--organize` or `-o`: Only organize the anime files into folders.

### Example Commands

1. **Rename and Organize Files:**
   ```bash
   python pahesort.py --all /path/to/your/anime/files

2. **Only Rename Files:**
   ```bash
   python pahesort.py --rename /path/to/your/anime/files

3. **Only Organize Files:**
   ```bash
   python pahesort.py --organize /path/to/your/anime/files

## Contributing

Feel free to contribute by submitting issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

