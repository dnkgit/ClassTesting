
class StringTable:

    def __init__(self, initStrings, debugSetting):
        self.stringTable = initStrings[:]
        self.original_initStrings = initStrings[:]
        self.doDebug = debugSetting
        if self.doDebug:
            print("\nDisplayData INIT")
            print(self.stringTable)
            print(self.original_initStrings)

    def get_stringTableSize(self):
        if self.doDebug:
            print("\nget_stringTableSize")
        return len(self.stringTable)

    def set_stringTableEntry(self, entry, newString):
        if self.doDebug:
            print("\nset_stringTableEntry")
        if entry < len(self.stringTable):
            self.stringTable[entry] = newString

    def get_stringTableEntry(self, entry):
        if self.doDebug:
            print("\nget_stringTableEntry")
        if entry < len(self.stringTable):
            return self.stringTable[entry]

    def get_stringTable(self):
        if self.doDebug:
            print("\nget_stringTable")
        return self.stringTable

    def restore_initStrings(self):
        if self.doDebug:
            print("\nrestore_initStrings")
        self.stringTable = self.original_initStrings[:]
        if self.doDebug:
            print(self.stringTable)
            print(self.original_initStrings)

    def show_stringTable(self):
        if self.doDebug:
            print("\nshow_stringTable")
        for item in range(0, len(self.stringTable)):
            print(self.stringTable[item])

