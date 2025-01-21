std::string getenv(const std::string& name, const std::string& default_value) {
        const char* value = std::getenv(name.c_str());
        return value ? value : default_value;
    }

