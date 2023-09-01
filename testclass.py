import dummy1

localStrings = ['String1', 'String2', 'String3', 'String4']
disp2Strings = localStrings[::-1]

print("Start")
print(localStrings)
tStrings = localStrings[:]
tStrings[1] = 'Blow'
print(tStrings)

print("+1")
print(localStrings)
print(tStrings)

print("Test")
disp = dummy1.StringTable(localStrings, debugSetting=False)
disp2 = dummy1.StringTable(disp2Strings, debugSetting=False)
disp.show_stringTable()
disp2.show_stringTable()

disp.set_stringTableEntry(entry=2, newString='Time and Date')
disp.show_stringTable()

disp.restore_initStrings()
disp.show_stringTable()

print(disp.get_stringTableSize())
print(disp.get_stringTableEntry(0))
print(disp.get_stringTableEntry(3))