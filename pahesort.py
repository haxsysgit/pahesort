import os
import shutil
import re
import argparse

def gather_anime(path: str):
    """
    Moves files that start with 'AnimePahe' to a new directory named 'AnimePahe'.
    
    Args:
        path (str): The path where the AnimePahe files are located.
        
    Returns:
        str: The path to the 'AnimePahe' folder where files have been moved.
    """
    if path:
        os.chdir(path)
        
    animepahe_files = [filename for filename in os.listdir(path) if filename.startswith("AnimePahe")]
    
    animepahe_folder = os.path.join(path, "AnimePahe")
    
    if not os.path.exists(animepahe_folder):
        os.mkdir(animepahe_folder)

    for file in animepahe_files:
        filepath = os.path.join(path, file)
        shutil.move(filepath, animepahe_folder)

    return animepahe_folder

def rename_anime(path: str, animepahe: bool = False):
    """
    Renames anime files to a standard format. The format is:
    "EpisodeNumber-AnimeName-Quality.ext". Optionally moves files from the 'AnimePahe' folder.
    
    Args:
        path (str): The path where the anime files are located.
        animepahe (bool): Whether the files are in an 'AnimePahe' folder (default: False).
    """
    if animepahe:
        folder_path = gather_anime(path)
        os.chdir(folder_path)
    else:
        folder_path = path
        os.chdir(path)
    
    animeinpath = [pahe for pahe in os.listdir() if os.path.isfile(pahe)]
    
    if animeinpath:
        for file in animeinpath:
            anime, ext = os.path.splitext(file)
            if ext in ['.mp4', '.mkv', '.avi'] and anime.startswith('AnimePahe'):
                anime_split = list(filter(None, (anime.replace('AnimePahe_', '').replace('-', '').split('_'))))
                
                if len(anime_split) > 1:
                    integer_index = 0

                    for i, x in enumerate(anime_split):
                        if x.isdigit():
                            integer_index = i

                    try:
                        formatted_integer = str(int(anime_split[integer_index])).zfill(2)
                        animename_list = anime_split[:integer_index]
                        animename = animename_list[:3] if len(animename_list) > 4 else animename_list
                        quality = anime_split[integer_index+1]
                        new_filename = f"{formatted_integer}-{'_'.join(animename)}-{quality}{ext}"
                    except:
                        print(f"This file -> {file} , should be manually renamed")
                        continue

                    os.rename(file, new_filename)
                    print(f"Renamed {file} --> {new_filename}\n")
    else:
        print(f"\nAll Animepahe file has been renamed\n\nDirectory Cleaned -> {path}\nFiles Current path -> {folder_path}")

def organize_anime(path: str, animepahe: bool = False):
    """
    Organizes anime files into folders based on their name. Creates folders named after the anime name.
    
    Args:
        path (str): The path where the anime files are located.
        animepahe (bool): Whether the files are in an 'AnimePahe' folder (default: False).
    """
    if animepahe:
        folder_path = gather_anime(path)
    else:
        folder_path = path

    os.chdir(folder_path)
    anime_files = [file for file in os.listdir() if os.path.isfile(file)]
    
    for file in anime_files:
        match = re.match(r"^\d+-(.*?)-\d+p", file)

        if match:
            anime_name = match.group(1).strip()
        else:
            print(f"Skipping file: {file} (doesn't match expected format)")
            continue

        anime_folder = os.path.join(folder_path, anime_name)
        
        if not os.path.exists(anime_folder):
            os.mkdir(anime_folder)

        shutil.move(file, os.path.join(anime_folder, file))
        print(f"\nMoved {file} to {anime_folder}")

def main():
    """
    Main function to handle command-line arguments and execute the appropriate functions.
    """
    parser = argparse.ArgumentParser(description="Process and organize anime files.")
    parser.add_argument("path", help="Specify the path where the anime files exist", type=str, nargs='?')
    parser.add_argument("-a","--all", help="Perform all operations: transfer, rename, and organize", action='store_true')
    parser.add_argument("-r","--rename", help="Only rename the anime files", action='store_true')
    parser.add_argument("-o","--organize", help="Only organize the anime files into folders", action='store_true')
    
    args = parser.parse_args()
    rearg = args.rename
    orgarg = args.organize
    patharg = args.path or "/home/haxsys/Downloads"

    if args.all:
        rename_anime(patharg, animepahe=True)
        organize_anime(patharg, animepahe=True)
    elif rearg:
        rename_anime(patharg)
    elif orgarg:
        organize_anime(patharg)
    else:
        print("\nNo operation specified. Use --all, --rename, or --organize.")
        
if __name__ == "__main__":
    main()
