# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

Initially some of the files had several issues but all were largely whitespace errors or line length errors and were easily fixed, prior to deployment.

> ![screenshot of validation errors](documentation/validation/validation_errors.png)

⚠️ Reconfirm all linter links show no errors before submission ⚠️

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
|  | [calc.py](https://github.com/geraldine-mor/row_assist/blob/main/calc.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/geraldine-mor/row_assist/main/calc.py) | ![screenshot of calc.py no issues](documentation/validation/calc_validation.png) |  |
|  | [inputs.py](https://github.com/geraldine-mor/row_assist/blob/main/inputs.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/geraldine-mor/row_assist/main/inputs.py) | ![screenshot of inputs.py no issues](documentation/validation/inputs_validation.png) |  |
|  | [ref_data.py](https://github.com/geraldine-mor/row_assist/blob/main/ref_data.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/geraldine-mor/row_assist/main/ref_data.py) | ![screenshot of ref_data.py no issues](documentation/validation/ref_data_validation.png) |  |
|  | [run.py](https://github.com/geraldine-mor/row_assist/blob/main/run.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/geraldine-mor/row_assist/main/run.py) | ![screenshot of run.py no issues](documentation/validation/run_validation.png) |  |
|  | [utils.py](https://github.com/geraldine-mor/row_assist/blob/main/utils.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/geraldine-mor/row_assist/main/utils.py) | ![screenshot of utils.py no issues](documentation/validation/utils_validation.png) |  |
|  | [validate.py](https://github.com/geraldine-mor/row_assist/blob/main/validate.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/geraldine-mor/row_assist/main/validate.py) | ![screenshot](documentation/validation/validate_validation.png) |  |


## Responsiveness

Due to the command-line nature of this application, traditional responsiveness testing across devices and screen sizes is not applicable.

## Browser Compatibility

This project is a Python command-line only application deployed via The Code Institue's web terminal interface. Browser compatibility testing focuses on whether the terminal interface renders correctly rather than application-specific functionality and as such is not applicable.

## Lighthouse Audit

Lighthouse audits are not applicable to this project since they do not test the Python command-line application but rather focus on the provided interface.

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing to ensure invalid or unexpected user input is handled with clear feedback and without causing the program to crash.

| Feature | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Age Input Validation | Feature is expected to reject non-numeric input. | Entered "forty" when prompted for the age. | Error message displayed: "Invalid age, please enter a number between 10 and 90" and re-prompted | ![screenshot of error message](documentation/defensive/age_forty.png) |
| | Feature is expected to reject age entries below minimum (10). | Entered "7" for the age. | Error message displayed: "I'm sorry, only ages between 10 and 90 can be accepted" and re-prompted. | ![screenshot of error message](documentation/defensive/age_7.png) |
|  | Feature is expected to reject age entries above the maximum (90). | Entered "92" for the age. | Error message displayed: "I'm sorry, only ages between 10 and 90 can be accepted" and re-prompted. | ![screenshot of error message](documentation/defensive/age_92.png) |
| | Feature is expected to accept valid age input at the boundaries. | Entered "10" and "90". | Both ages accepted without issue and program moved on to next step. | ![screenshot of successful input](documentation/defensive/age_10.png) ![screenshot of successful input](documentation/defensive/age_90.png) |
|  | Feature is expected to reject blank entries. | Pressed enter with no value entered. | Error message displayed: "Invalid age, please enter a number between 10 and 90" and re-prompted. | ![screenshot of error message](documentation/defensive/age_blank.png) |
| Gender Input Validation | Feature is expected to reject all non-alphabetic characters. | Entered "4" and "," for the gender. | Error message displayed both times: "Invalid entry, please enter either m or f" and re-prompted. | ![screenshot of error message](documentation/defensive/gender_4.png) ![screenshot of error message](documentation/defensive/gender_comma.png) |
|  | Feature is expected to reject any letter except "m" or "f". | Entered "g" for the gender. | Error message displayed: "Invalid entry, please enter either m or f" and re-prompted. | ![screenshot of error message](documentation/defensive/gender_g.png) |
|  | Feature is expected to reject multiple characters or words. | Entered "male" for the gender. | Error message displayed: "Invalid entry, please enter either m or f" and re-prompted. | ![screenshot of error message](documentation/defensive/gender_male.png) |
|  | Feature is expected to accept lowercase valid input. | Entered both "m" and "f" for gender. | Both values accepted without issue and program moved on to next step. | ![screenshot of successful input](documentation/defensive/gender_m.png)  ![screenshot of successful input](documentation/defensive/gender_f.png) |
|  | Feature is expected to accept uppercase valid input. | Entered both "M" and "F" for gender. | Both values accepted without issue and program moved on to next step. | ![screenshot of successful input](documentation/defensive/gender_M.png)  ![screenshot of successful input](documentation/defensive/gender_F.png) |
|  | Feature is expected to reject blank entries. | Pressed enter with no value entered. | Error message displayed: "Invalid entry, please enter either m or f" and re-prompted. | ![screenshot of error message](documentation/defensive/gender_blank.png) |
| Minutes Input Validation | Feature is expected to reject non-numeric characters. | Entered "z" for minutes. | Error message displayed: "Invalid entry, please enter a minutes value between 0 and 59" and re-prompted. | ![screenshot of error message](documentation/defensive/minutes_z.png) |
|  | Feature is expected to reject negative values | Entered "-3" for minutes. | Error message displayed: "Invalid entry, please enter a minutes value between 0 and 59" and re-prompted. | ![screenshot of error message](documentation/defensive/minutes_negative.png) |
|  | Feature is expected to reject values above 59 | Entered "64" for minutes. | Error message displayed: "Invalid entry, please enter a minutes value between 0 and 59" and re-prompted. | ![screenshot of error message](documentation/defensive/minutes_64.png) |
|  | Feature is expected to reject blank input | Pressed enter with no value entered. | Error message displayed: "Invalid entry, please enter a minutes value between 0 and 59" and re-prompted. | ![screenshot of error message](documentation/defensive/minutes_blank.png) |
|  | Feature is expected to accept valid minutes value at the boundaries | Entered "0" and "59" for minutes. | Both values accepted without issue and program moved on to next step. | ![screenshot of successful input](documentation/defensive/minutes_0.png) ![screenshot of successful input](documentation/defensive/minutes_59.png) |
| Seconds Input Validation | Feature is expected to reject non-numeric characters. | Entered "x" for seconds. | Error message displayed: "Invalid entry, please enter a seconds value between 0 and 59" and re-prompted. | ![screenshot of error message](documentation/defensive/seconds_x.png) |
|  | Feature is expected to reject negative values | Entered "-7" for seconds. | Error message displayed: "Invalid entry, please enter a seconds value between 0 and 59" and re-prompted. | ![screenshot of error message](documentation/defensive/seconds_negative.png) |
|  | Feature is expected to reject values above 59 | Entered "72" for seconds. | Error message displayed: "Invalid entry, please enter a seconds value between 0 and 59" and re-prompted. | ![screenshot of error message](documentation/defensive/seconds_72.png) |
|  | Feature is expected to reject blank input | Pressed enter with no value entered. | Error message displayed: "Invalid entry, please enter a seconds value between 0 and 59" and re-prompted. | ![screenshot of error message](documentation/defensive/seconds_blank.png) |
|  | Feature is expected to accept valid seconds values at the boundaries | Entered "0" and "59" for seconds. | Both values accepted without issue and program moved on to next step. | ![screenshot of successful input](documentation/defensive/seconds_0.png) ![screenshot of successful input](documentation/defensive/seconds_59.png) |
| Tenths Input Validation | Feature is expected to reject non-numeric characters. | Entered "d" for tenths. | Error message displayed: "Invalid entry, please enter a tenths value between 0 and 9" and re-prompted. | ![screenshot of error message](documentation/defensive/tenths_d.png) |
|  | Feature is expected to reject negative values | Entered "-1" for tenths. | Error message displayed: "Invalid entry, please enter a tenths value between 0 and 9" and re-prompted. | ![screenshot of error message](documentation/defensive/tenths_negative.png) |
|  | Feature is expected to reject values above 9. | Entered "12" for tenths. | Error message displayed: "Invalid entry, please enter a tenths value between 0 and 9" and re-prompted. | ![screenshot of error message](documentation/defensive/tenths_12.png) |
|  | Feature is expected to reject blank input. | Pressed enter with no value entered. | Error message displayed: "Invalid entry, please enter a tenths value between 0 and 9" and re-prompted. | ![screenshot of error message](documentation/defensive/tenths_blank.png) |
|  | Feature is expected to accept valid tenths values at the boundaries. | Entered "0" and "9" for tenths. | Both values accepted without issue and program moved on to next step. | ![screenshot of successful input](documentation/defensive/tenths_0.png) ![screenshot of successful input](documentation/defensive/tenths_9.png) |
| Program Restart | Feature is expected to restart the program with a clear screen when any key except "x" is entered. | Entered "w", "Insert" and "7" as well as no value. | All values initiated the program restart and cleared the visible window though scrolling upward revealed uncleared text (see [known issues](#known-issues)). | ![screenshot of restart](documentation/defensive/restart.png) |
| Program Exit | Feature is expected to safely close the program if "x" is entered. | Entered "x" and "X". | Program closed with no issues. | ![screenshot of closed program](documentation/defensive/exit_x.png) ![screenshot of closed program](documentation/defensive/exit_X.png) | 

### Edge Case Handling

| Feature | Test | Result | Screenshot |
| --- | --- | --- | --- |
| World Record Detection | Entered time faster than world record (5:35.8) | Humorous message displayed: "Greetings Barry Allen! The fastest 2k ever recorded is 5:35.8 and you smashed it!" | ![screenshot of world record message](documentation/wr_message.png) |

## User Story Testing

⚠️ Pick Up Here ⚠️

Testing User Stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **Features** should already align with the **User Stories**, so this should be as simple as creating a table with the User Story, matching with the re-used screenshot from the respective Feature.

⚠️ --- END --- ⚠️

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a user | I would like to input the number of each sandwich type sold during the day | so that I can track daily sales accurately. | ![screenshot](documentation/features/feature01.png) |
| As a user | I would like to view a breakdown of total sandwich sales by type | so that I can easily see which sandwiches are the most and least popular. | ![screenshot](documentation/features/feature02.png) |
| As a user | I would like the application to calculate the total sandwiches sold for the day | so that I don’t have to do manual sums. | ![screenshot](documentation/features/feature03.png) |
| As a user | I would like to see a trend of sandwich sales over time (e.g., week, month) | so that I can identify which sandwiches are consistently popular. | ![screenshot](documentation/features/feature04.png) |
| As a user | I would like the application to suggest an estimated number of each sandwich type to make for the next day, based on past sales data | so that I can minimize waste and shortages. | ![screenshot](documentation/features/feature05.png) |
| As a user | I would like the app to categorize sandwiches by type (e.g., vegetarian, meat, cheese) | so that I can track popularity within different dietary categories. | ![screenshot](documentation/features/feature06.png) |
| As a user | I would like to input sales quickly with minimal typing | so that I can focus on running the shop instead of logging data. | ![screenshot](documentation/features/feature07.png) |
| As a user | I would like the app to be intuitive and easy to use | so that I can start tracking sales without needing extensive training. | ![screenshot](documentation/features/feature08.png) |

## Bugs

⚠️ INSTRUCTIONS ⚠️

Nobody likes bugs,... except the assessors! Projects seem more suspicious if a student doesn't properly track their bugs. If you're about to submit your project without any bugs listed below, you should ask yourself why you're doing this course in the first place, if you're able to build this entire application without running into any bugs. The best thing you can do for any project is to document your bugs! Not only does it show the true stages of development, but think of it as breadcrumbs for yourself in the future, should you encounter the same/similar bug again, it acts as a gentle reminder on what you did to fix the bug.

If/when you encounter bugs during the development stages of your project, you should document them here, ideally with a screenshot explaining what the issue was, and what you did to fix the bug.

Alternatively, an improved way to manage bugs is to use the built-in **[Issues](https://www.github.com/geraldine-mor/row_assist/issues)** tracker on your GitHub repository. This can be found at the top of your repository, the tab called "Issues".

If using the Issues tracker for bug management, you can simplify the documentation process for testing. Issues allow you to directly paste screenshots into the issue page without having to first save the screenshot locally. You can add labels to your issues (e.g. `bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s). Once you've solved the issue/bug, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following examples below.

⚠️ --- END --- ⚠️

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/geraldine-mor/row_assist?query=is%3Aissue%20is%3Aclosed%20label%3Abug&label=Fixed%20Bugs&color=green)](https://www.github.com/geraldine-mor/row_assist/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/geraldine-mor/row_assist/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/geraldine-mor/row_assist/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.png)

### Unfixed Bugs

⚠️ INSTRUCTIONS ⚠️

You will need to mention any unfixed bugs and why they are not fixed upon submission of your project. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. Where possible, you must fix all outstanding bugs, unless outside of your control.

If you've identified any unfixed bugs, no matter how small, be sure to list them here! It's better to be honest and list them, because if it's not documented and an assessor finds the issue, they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

⚠️ --- END --- ⚠️

[![GitHub issue custom search](https://img.shields.io/github/issues-search/geraldine-mor/row_assist?query=is%3Aissue%2Bis%3Aopen%2Blabel%3Abug&label=Unfixed%20Bugs&color=red)](https://www.github.com/geraldine-mor/row_assist/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

Any remaining open issues can be tracked [here](https://www.github.com/geraldine-mor/row_assist/issues?q=is%3Aissue+is%3Aopen+label%3Abug).

![screenshot](documentation/bugs/gh-issues-open.png)

### Known Issues

| Issue | Screenshot |
| --- | --- |
| The project is designed to be responsive from `375px` and upwards, in line with the material taught on the course LMS. Minor layout inconsistencies may occur on extra-wide (e.g. 4k/8k monitors), or smart-display devices (e.g. Nest Hub, Smart Watches, Gameboy Color, etc.), as these resolutions are outside the project’s scope, as taught by Code Institute. | ![screenshot](documentation/issues/poor-responsiveness.png) |
| When using a helper `clear()` function, any text above the height of the terminal (24 lines) does not clear, and remains when scrolling up. | ![screenshot](documentation/issues/clear-scrolling.png) |
| The `colorama` terminal colors are fainter on Heroku when compared to the IDE locally. | ![screenshot](documentation/issues/colorama.png) |
| Emojis are cut-off when viewing the application from Firefox. | ![screenshot](documentation/issues/emojis.png) |
| The Python terminal doesn't work well with Safari, and sometimes uses cannot type in the application. | ![screenshot](documentation/issues/safari.png) |
| If a user types `CTRL`+`C` in the terminal on the live site, they can manually stop the application and receive and error. | ![screenshot](documentation/issues/ctrl-c.png) |

> [!IMPORTANT]  
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.

