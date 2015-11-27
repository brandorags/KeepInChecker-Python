class CommandLineUtilities(object):
    """
    A utility class for manipulating command line data.
    """

    @staticmethod
    def convert_output_to_string(output_object):
        """
        Returns a string representation of standard output from the command line. In order
        to remove the newline character, splitting it from the rest of the output is mandatory.
        """
        return output_object.stdout.read().decode('utf-8').split('\n')[0]
