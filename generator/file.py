from generator import clf_string, combined_log_format_string, generator, gen_random_template
from utils import write_file, chance_choose
import parameters

# Returns a random template, a CLF template, or a Combined Log Format template
def get_template():
    return chance_choose(
        combined_log_format_string,
        chance_choose(
            clf_string,
            gen_random_template(),
            parameters.frequency['CLF_template']),
        parameters.frequency['combined_log_format_template'])


def templates_to_logs(templates, test_mode=False):
    # Turns all of the templates into a list of tab-separated strings
    # of the log and its truth, e.g.:
    # [
    #   'hello_world/hi 123\tUUUUUUUUUUUUUU_bbb',
    #   '456 howdy/hi/m.jpg\tbbb_UUUUUUUUUUUUUU',
    # ]
    return map(
        lambda template: '\t'.join(
            generator(
                template=template, test_mode=test_mode)),
        templates)


def write_split_files(out_file, lines, train_set_percentage):
    num_train_lines = round(lines * (train_set_percentage / 100))
    num_test_lines = lines - num_train_lines

    # First gen the test templates as there will likely be fewer test templates
    # to go through than training templates
    test_templates = []
    for _ in range(num_test_lines):
        # Note that there are no CLF templates here
        test_templates.append(gen_random_template())

    train_templates = []
    for _ in range(num_train_lines):
        template = get_template()

        # Ensure that the random template (or CLF template) is NOT in the test
        # templates (ensures uniqueness from test templates)
        while template in test_templates:
            template = get_template()

        train_templates.append(template)

    write_file('{}.train.txt'.format(out_file), '\n'.join(templates_to_logs(train_templates, test_mode=False)) + '\n')
    write_file('{}.test.txt'.format(out_file), '\n'.join(templates_to_logs(test_templates, test_mode=True)) + '\n')


def write_joint_file(out_file, lines, combined_only=False):
    templates = []

    for _ in range(lines):
        # If the flag to generate every line in CombinedLF is set, only generate CombinedLF
        if combined_only:
            templates.append(combined_log_format_string)
        else:
            # 40% chance it will be a Combined Log Format
            # From there, 40% chance it will be the CLF-formatted string versus a random template
            templates.append(get_template())

    write_file(out_file, '\n'.join(templates_to_logs(templates)) + '\n')

def main(out_file: "The name of the file that the lines will be output into, e.g. `logs.txt`",
         lines: ("The number of lines to output", 'option', 'l') = 100,
         split_train_test: ("Outputs a train set file and a test set file, instead of a single file", 'flag', 's') = False,
         train_set_percentage: ("Percent of the observations to use for training", 'option', 'p') = 90,
         combined_only: ("Only generate lines in Combined Log Format", 'flag', 'clf') = False):
    
    if split_train_test:
        write_split_files(out_file, lines, train_set_percentage)
    else:
        write_joint_file(out_file, lines, combined_only)


if __name__ == "__main__":
    import plac

    plac.call(main)
