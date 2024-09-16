"""
Write tests for 2_python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
import os
import tempfile
from task_read_write import read_and_extract_values, write_to_output_file


def test_read_and_extract_values(tmpdir):
    # Create temporary files with specific content
    file_contents = ["80", "39", "67"]
    file_paths = []
    folder_path = tmpdir / "files"
    os.makedirs(folder_path)
    for i, content in enumerate(file_contents):
        file_path = folder_path.join(f"file_{i + 1}.txt")
        file_path.write(content)
        file_paths.append(str(file_path))

    # Test the read_and_extract_values function
    values = read_and_extract_values(str(tmpdir))
    
    # Ensure that the extracted values match the expected values
    assert values == ["80", "39", "67"]

def test_write_to_output_file(tmpdir):
    # Test the write_to_output_file function
    values = ["80", "39", "67"]
    output_file = tmpdir.join("result.txt")
    write_to_output_file(values, str(output_file))

    # Read the content of the written file
    result_content = output_file.read()

    # Ensure that the content of the written file matches the expected result
    assert result_content == "80, 39, 67"
