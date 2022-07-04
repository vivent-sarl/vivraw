import cliprompts
from pyfiglet import Figlet
import os
from vivraw.raw import read_from_raw_file, convert_to_mv, write_mv_data_to_parquet
from datetime import datetime, timedelta
import pandas as pd

f = Figlet(font="big")

print(f.renderText("Vivent raw2parquet"))

if __name__ == "__main__":

    cli_input_params = {}
    cliprompts.ask_about_run_metadata(cli_input_params)

    for i in range(cli_input_params["channels"]):

        channel = i + 1
        raw_filepath = f"{cli_input_params['input_path']}/{channel}"
        raw_files = os.listdir(raw_filepath)
        raw_files.sort()

        plant_id = f"{cli_input_params['plant_id'][:-1]}{channel}"

        for raw_filename in raw_files:
            mv = convert_to_mv(
                read_from_raw_file(os.path.join(raw_filepath, raw_filename)),
                cli_input_params["mv_span"],
            )[:-1]

            start = datetime.utcfromtimestamp(int(raw_filename.replace(".raw", "")))
            stop = start + timedelta(minutes=mv.shape[0])

            df = pd.DataFrame(
                {"timestamp": pd.date_range(start, stop, mv.shape[0]), "mV": mv}
            )
            
            if cli_input_params["resolution"] == "5min":
                df.set_index("timestamp", inplace=True)
                df = df.resample("5T").mean()
                df.reset_index(inplace=True)

            write_mv_data_to_parquet(
                shard=df["mV"].to_numpy(),
                timestamps=df["timestamp"].to_numpy(),
                timezone=cli_input_params["timezone"],
                target_data_directory=cli_input_params["output_path"],
                plant_id=plant_id,
            )
