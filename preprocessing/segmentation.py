import os
os.environ["JAVA_HOME"] = '../java/jdk-17.0.7'
# os.environ["JAVA_HOME"] = 'java/openjdk-14.0.1.jdk/Contents/Home'

import cellprofiler_core.pipeline
import cellprofiler_core.preferences
import cellprofiler_core.utilities.java
import pathlib

cellprofiler_core.preferences.set_headless()
cellprofiler_core.utilities.java.start_java()
pipeline = cellprofiler_core.pipeline.Pipeline()
pipeline.load("segmentation_deep.cppipe")
data_dir = '/n/data1/hms/dbmi/zitnik/lab/users/kel331/microscopyclock/data/raw/test/Plate/1/2023-08-08/16767/TimePoint_1'
file_list = list(pathlib.Path(data_dir).absolute().glob('*.tif'))
file_list_clean = []
for f in file_list:
    if "thumb" not in str(f):
        file_list_clean.append(f)
files = [file.as_uri() for file in file_list_clean]
pipeline.read_file_list(files)
current_dir = pathlib.Path().absolute()
cellprofiler_core.preferences.set_default_output_directory("/n/data1/hms/dbmi/zitnik/lab/users/kel331/microscopyclock/data/cropped/test/1")
output_measurements = pipeline.run()
