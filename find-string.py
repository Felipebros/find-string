import locale
import mimetypes
import os
import time
import sys


def search_string_in_files(folder_path, string_to_search):
    results = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if (
                "text" in str(mimetypes.guess_type(file)[0]).lower() or
                str(mimetypes.guess_type(file)[0]).lower() in ["none"]
            ):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if string_to_search in line:
                            result = f"String encontrada no arquivo {file_path}, linha {i+1}: {line}"
                            results.append(result)
    return results


def human_name_time(time):
    unit_measurement = "segundos"
    if time < 1:
        time *= 1000
        unit_measurement = "ms"
    return f"{locale.format_string('%.2f', time)} {unit_measurement}"


if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, '')

    start_time_total = time.time()

    if len(sys.argv) == 2:
        string_to_search = sys.argv[1]
        folder_path = "."
    elif len(sys.argv) == 3:
        string_to_search = sys.argv[1]
        folder_path = sys.argv[2]
    else:
        print("Erro: você deve especificar a string de pesquisa como o primeiro argumento.")
        sys.exit()

    with open("resultados.txt", "w") as final_file:
        results = search_string_in_files(folder_path, string_to_search)

        end_time_total = time.time()
        query_time_total = end_time_total - start_time_total
        print(f"Total de resultados encontrados: {len(results)}")
        print(f"Em {human_name_time(query_time_total)}")
        results.append(f"Total de resultados encontrados: {len(results)}")
        results.append(f"Em {human_name_time(query_time_total)}")

        for result in results:
            final_file.write(result + "\n")
