class KeyValueStore:
    def __init__(self):
        self._data = {}

    def __setitem__(self, key, value):
        self._data[key] = value
        self._log_change(key, value)

    def __getitem__(self, key):
        return self._data[key]

    def __delitem__(self, key):
        value = self._data.pop(key)
        self._log_change(key, value, deleted=True)

    def _log_change(self, key, value, deleted=False):
        action = "Deleted" if deleted else "Added/Updated"
        with open("log.txt", "a") as log_file:
            log_file.write(f"{action}: Key = {key}, Value = {value}\n")

    def __repr__(self):
        return repr(self._data)

# Example usage
store = KeyValueStore()

store["name"] = "Alice"
store["age"] = 30
print(store)

del store["name"]
print(store)
