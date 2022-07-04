from PyInquirer import style_from_dict, Token, prompt

style = style_from_dict(
    {
        Token.QuestionMark: "#E91E63 bold",
        Token.Selected: "#673AB7 bold",
        Token.Instruction: "",
        Token.Answer: "#2196f3 bold",
        Token.Question: "",
    }
)


def ask_about_run_metadata(cli_input_params):

    save_answers_about_data_directories(cli_input_params)
    save_answers_about_device_metadata(cli_input_params)


def save_answers_about_data_directories(cli_input_params):
    questions = [
        {
            "type": "input",
            "name": "input_path",
            "message": "What is the absolute path of the raw directories to convert?",
        },
        {
            "type": "input",
            "name": "output_path",
            "message": "What is the absolute path of the parquet directory we will write to?",
        },
        {
            "type": "list",
            "name": "resolution",
            "message": "What should the output resolution of the parquet data be?",
            "choices": ["1min", "5min"],
        },
    ]
    answers = prompt(questions, style=style)

    cli_input_params["input_path"] = answers["input_path"]
    cli_input_params["output_path"] = answers["output_path"]
    cli_input_params["resolution"] = answers["resolution"]


def save_answers_about_device_metadata(cli_input_params):
    questions = [
        {
            "type": "list",
            "name": "mv_span",
            "message": "What is the millivolt span of the device?",
            "choices": ["5000", "105000"],
        },
        {
            "type": "list",
            "name": "channels",
            "message": "How many channels does the device have?",
            "choices": ["2", "8"],
        },
        {
            "type": "input",
            "name": "plant_id",
            "message": "What should the datalake plant_ids look like? An example is viv-trial0-253def-*",
        },
        {
            "type": "input",
            "name": "timezone",
            "message": "What is the numerical device timezone offset from UTC?",
        },
    ]
    answers = prompt(questions, style=style)

    cli_input_params["mv_span"] = int(answers["mv_span"])
    cli_input_params["channels"] = int(answers["channels"])
    cli_input_params["plant_id"] = answers["plant_id"]
    cli_input_params["timezone"] = int(answers["timezone"])
