import yaml

def get_congig():
    try:
        config_file_path = "config.yml"
        
        with open(config_file_path, 'r') as stream:
            config = yaml.safe_load(stream)
        
        return config   
    except Exception as e:
        st.error("🚨 Error while loading config: " + str(e.args))

def get_embeddings():
    pass

def get_llm():
    pass