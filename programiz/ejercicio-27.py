def jazzify_chords(chords):
    result = []
    for chord in chords:
        if chord.endswith("7"):
            result.append(chord)
        else:
            result.append(chord+"7")
    return result