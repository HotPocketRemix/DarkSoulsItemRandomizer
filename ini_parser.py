import configparser

def get_values_from_ini(ini_file, section="DEFAULT"):
    config = configparser.ConfigParser()
    config.read(ini_file)

    if section in config:       #check if section in ini
        return config[section]
    else:
        return config["DEFAULT"]

def save_ini(ini_file, options):
    config = configparser.ConfigParser()
    for k,v in vars(options).items():
        config["DEFAULT"][k] = str(v)       #values must be strings to write
    
    with open(ini_file, 'w') as configfile:
        config.write(configfile)

def get_option_value(config, k):
    """ 
        The following parses the values in the ini to produce the option list in the correct format
        While I could create a separate list/dict to specify the typing of the data coming in
            or by creating a section in the inifile for the typing
        This would add extra work to the developer who adds new features which I think is far more annoying
        So instead we get this ugly mess of try/excepts to get the typing we actually care about: int -> bool -> string
        TODO: Allow type to be specified when calling (not really important at all)
    """
    try:
        option = config.getint(k, 0)
    except ValueError:
        try:
            option = config.getboolean(k, False)
        except ValueError:
            option = config.get(k, "No Default Value")

    return option
