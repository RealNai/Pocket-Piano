left_hand = ['Z', 'S', 'X', 'D', 'C', 'V', 'G', 'B', 'H', 'N', 'J', 'M']
#right_hand = ['R', '5', 'T', '6', 'Y', 'U', '8', 'I', '9', 'O', '0', 'P']
right_hand = ['K', 'L', ':', ';', '-', '=', '8', 'I', '9', 'O', '0', 'P']
keybinds = ['1', '2', '3', '4' ,'5', '6', '7', 'T', 'W', 'R', 'Y']

keys = ['C','D','E','F','G','A','B','C#','D#','F#','G#','A#']
key_all = ['C','D','E','F','G','A','B','C#','D#','F#','G#','A#','Db','Eb','Gb','Ab','Bb']

key_dict = {'C':[[['w', 9, 0], ['w', 11, 0], ['w', 13, 0], ['w', 16, 0]], 
                 [['w', 10, 0], ['w', 12, 0], ['w', 14, 0], ['w', 16, 0]], 
                 [['w', 11, 0], ['w', 13, 0], ['w', 15, 0], ['w', 17, 0]], 
                 [['w', 12, 0], ['w', 14, 0], ['w', 16, 0], ['w', 19, 0]], 
                 [['w', 13, 0], ['w', 15, 0], ['w', 17, 0], ['w', 20, 0]], 
                 [['w', 14, 0], ['w', 16, 0], ['w', 18, 0], ['w', 20, 0]], 
                 [['w', 15, 0], ['w', 17, 0], ['b', 13, 0], ['w', 21, 0]], 
                 [['b', 9, 0], ['w', 15, 0], ['w', 17, 0], ['w', 19, 0]] ,
                   [['b', 8, 0], ['b', 10, 0], ['b', 11, 0], ['w', 18, 0]], # 5/6
                   [['w', 14, 0], ['w', 16, 0], ['w', 18, 0], ['w', 20, 0]], # 2/4
                   [['w', 17, 0], ['b', 13, 0], ['w', 21, 0], ['w', 23, 0]]], #5/4

            'D':[[['w', 10, 0], ['b', 8, 0], ['w', 14, 0], ['w', 17, 0]],
             [['w', 11, 0], ['w', 13, 0], ['w', 15, 0], ['w', 17, 0]],
              [['b', 8, 0], ['w', 14, 0], ['b', 11, 0], ['w', 18, 0]],
               [['w', 13, 0], ['w', 15, 0], ['w', 17, 0], ['w', 20, 0]],
                [['w', 14, 0], ['b', 11, 0], ['w', 18, 0], ['w', 21, 0]],
                 [['w', 15, 0], ['w', 17, 0], ['b', 13, 0], ['w', 21, 0]],
                  [['b', 11, 0], ['w', 18, 0], ['b', 14, 0], ['w', 22, 0]],
                   [['b', 10, 0], ['b', 11, 0], ['w', 18, 0], ['w', 20, 0]],
                   [['b', 8, 0], ['b', 10, 0], ['b', 11, 0], ['w', 18, 0]], # 5/6
                   [['w', 14, 0], ['w', 16, 0], ['w', 18, 0], ['w', 20, 0]], # 2/4
                   [['w', 17, 0], ['b', 13, 0], ['w', 21, 0], ['w', 23, 0]]], #5/4

            'E':[[['w', 11, 0], ['b', 9, 0], ['w', 15, 0], ['w', 18, 0]],
             [['b', 8, 0], ['w', 14, 0], ['b', 11, 0], ['w', 18, 0]],
              [['b', 9, 0], ['w', 15, 0], ['b', 12, 0], ['b', 13, 0]],
               [['w', 14, 0], ['b', 11, 0], ['w', 18, 0], ['w', 21, 0]],
                [['w', 15, 0], ['b', 12, 0], ['b', 13, 0], ['w', 22, 0]],
                 [['b', 11, 0], ['w', 18, 0], ['b', 14, 0], ['w', 22, 0]],
                  [['w', 17, 0], ['w', 19, 0], ['w', 21, 0], ['w', 23, 0]],
                  [['w', 16, 0], ['b', 12, 0], ['b', 13, 0], ['w', 21, 0]],
                   [['b', 8, 0], ['b', 10, 0], ['b', 11, 0], ['w', 18, 0]], # 5/6
                   [['w', 14, 0], ['w', 16, 0], ['w', 18, 0], ['w', 20, 0]], # 2/4
                   [['w', 17, 0], ['b', 13, 0], ['w', 21, 0], ['w', 23, 0]]], #5/4

            'F':[[['w', 12, 0], ['w', 14, 0], ['w', 16, 0], ['w', 19, 0]],
             [['w', 13, 0], ['b', 10, 0], ['w', 17, 0], ['w', 19, 0]],
              [['w', 14, 0], ['w', 16, 0], ['w', 18, 0], ['w', 20, 0]],
               [['b', 10, 0], ['w', 17, 0], ['w', 19, 0], ['b', 15, 0]],
                [['w', 16, 0], ['w', 18, 0], ['w', 20, 0], ['w', 23, 0]],
                 [['w', 17, 0], ['w', 19, 0], ['w', 21, 0], ['w', 23, 0]],
                  [['w', 18, 0], ['w', 20, 0], ['w', 22, 0], ['w', 24, 0]],
                   [['b', 11, 0], ['w', 18, 0], ['w', 20, 0], ['b', 15, 0]],
                   [['b', 8, 0], ['b', 10, 0], ['b', 11, 0], ['w', 18, 0]], # 5/6
                   [['w', 14, 0], ['w', 16, 0], ['w', 18, 0], ['w', 20, 0]], # 2/4
                   [['w', 17, 0], ['b', 13, 0], ['w', 21, 0], ['w', 23, 0]]], #5/4

            'G':[[['w', 13, 0], ['w', 15, 0], ['w', 17, 0], ['w', 20, 0]],
             [['w', 14, 0], ['w', 16, 0], ['w', 18, 0], ['w', 20, 0]], 
             [['w', 15, 0], ['w', 17, 0], ['b', 13, 0], ['w', 21, 0]],
              [['w', 16, 0], ['w', 18, 0], ['w', 20, 0], ['w', 23, 0]],
               [['w', 17, 0], ['b', 13, 0], ['w', 21, 0], ['w', 24, 0]],
                [['w', 18, 0], ['w', 20, 0], ['w', 22, 0], ['w', 24, 0]],
                 [['b', 13, 0], ['w', 21, 0], ['b', 16, 0], ['w', 25, 0]],
                  [['b', 12, 0], ['b', 13, 0], ['w', 21, 0], ['w', 23, 0]],
                   [['b', 8, 0], ['b', 10, 0], ['b', 11, 0], ['w', 18, 0]], # 5/6
                   [['w', 14, 0], ['w', 16, 0], ['w', 18, 0], ['w', 20, 0]], # 2/4
                   [['w', 17, 0], ['b', 13, 0], ['w', 21, 0], ['w', 23, 0]]], #5/4

            'A':[[['w', 14, 0], ['b', 11, 0], ['w', 18, 0], ['w', 21, 0]],
             [['w', 15, 0], ['w', 17, 0], ['b', 13, 0], ['w', 21, 0]],
              [['b', 11, 0], ['w', 18, 0], ['b', 14, 0], ['w', 22, 0]],
               [['w', 17, 0], ['b', 13, 0], ['w', 21, 0], ['w', 24, 0]],
                [['w', 18, 0], ['b', 14, 0], ['w', 22, 0], ['w', 25, 0]],
                 [['b', 13, 0], ['w', 21, 0], ['b', 16, 0], ['w', 25, 0]],
                  [['b', 14, 0], ['w', 22, 0], ['b', 17, 0], ['b', 18, 0]],
                   [['w', 19, 0], ['b', 14, 0], ['w', 22, 0], ['w', 24, 0]],
                   [['b', 8, 0], ['b', 10, 0], ['b', 11, 0], ['w', 18, 0]], # 5/6
                   [['w', 14, 0], ['w', 16, 0], ['w', 18, 0], ['w', 20, 0]], # 2/4
                   [['w', 17, 0], ['b', 13, 0], ['w', 21, 0], ['w', 23, 0]]], #5/4


            'B':[[['w', 8, 0], ['b', 7, 0], ['b', 8, 0], ['w', 15, 0]],
             [['b', 6, 0], ['w', 11, 0], ['b', 9, 0], ['w', 15, 0]],
             [['b', 7, 0], ['b', 8, 0], ['b', 10, 0], ['b', 11, 0]],
              [['w', 11, 0], ['b', 9, 0], ['w', 15, 0], ['w', 18, 0]],
               [['b', 8, 0], ['b', 10, 0], ['b', 11, 0], ['b', 13, 0]],
                [['b', 9, 0], ['w', 15, 0], ['b', 12, 0], ['b', 13, 0]],
                [['b', 10, 0], ['b', 11, 0], ['w', 19, 0], ['b', 14, 0]],
                 [['w', 13, 0], ['b', 10, 0], ['b', 11, 0], ['w', 18, 0]],
                   [['b', 8, 0], ['b', 10, 0], ['b', 11, 0], ['w', 18, 0]], # 5/6
                   [['w', 14, 0], ['w', 16, 0], ['w', 18, 0], ['w', 20, 0]], # 2/4
                   [['w', 17, 0], ['b', 13, 0], ['w', 21, 0], ['w', 23, 0]]], #5/4

            'C#':[[['b', 6, 0], ['w', 12, 0], ['b', 9, 0], ['b', 11, 0]],
             [['b', 7, 0], ['b', 8, 0], ['b', 10, 0], ['b', 11, 0]],
              [['w', 12, 0], ['b', 9, 0], ['w', 16, 0], ['b', 12, 0]],
               [['b', 8, 0], ['b', 10, 0], ['b', 11, 0], ['b', 13, 0]], 
               [['b', 9, 0], ['w', 16, 0], ['b', 12, 0], ['b', 14, 0]],
                [['b', 10, 0], ['b', 11, 0], ['w', 19, 0], ['b', 14, 0]],
                 [['w', 16, 0], ['b', 12, 0], ['w', 20, 0], ['b', 15, 0]],
                  [['w', 14, 0], ['w', 16, 0], ['b', 12, 0], ['b', 13, 0]],
                   [['b', 8, 0], ['b', 10, 0], ['b', 11, 0], ['w', 18, 0]], # 5/6
                   [['w', 14, 0], ['w', 16, 0], ['w', 18, 0], ['w', 20, 0]], # 2/4
                   [['w', 17, 0], ['b', 13, 0], ['w', 21, 0], ['w', 23, 0]]], #5/4

            'D#':[[['b', 7, 0], ['w', 13, 0], ['b', 10, 0], ['b', 12, 0]],
             [['w', 12, 0], ['b', 9, 0], ['w', 16, 0], ['b', 12, 0]],
              [['w', 13, 0], ['b', 10, 0], ['w', 17, 0], ['w', 19, 0]], 
              [['b', 9, 0], ['w', 16, 0], ['b', 12, 0], ['b', 14, 0]],
              [['b', 10, 0], ['w', 17, 0], ['w', 19, 0], ['b', 15, 0]], 
              [['w', 16, 0], ['b', 12, 0], ['w', 20, 0], ['b', 15, 0]], 
              [['w', 17, 0], ['w', 19, 0], ['w', 21, 0], ['w', 23, 0]], 
              [['w', 15, 0], ['w', 17, 0], ['w', 19, 0], ['b', 14, 0]],
                   [['b', 8, 0], ['b', 10, 0], ['b', 11, 0], ['w', 18, 0]], # 5/6
                   [['w', 14, 0], ['w', 16, 0], ['w', 18, 0], ['w', 20, 0]], # 2/4
                   [['w', 17, 0], ['b', 13, 0], ['w', 21, 0], ['w', 23, 0]]], #5/4

            'F#':[[['b', 8, 0], ['b', 10, 0], ['b', 11, 0], ['b', 13, 0]],
             [['b', 9, 0], ['w', 15, 0], ['b', 12, 0], ['b', 13, 0]],
              [['b', 10, 0], ['b', 11, 0], ['w', 19, 0], ['b', 14, 0]], 
              [['w', 15, 0], ['b', 12, 0], ['b', 13, 0], ['w', 22, 0]],
               [['b', 11, 0], ['w', 19, 0], ['b', 14, 0], ['b', 16, 0]],
                [['b', 12, 0], ['b', 13, 0], ['b', 15, 0], ['b', 16, 0]],
                 [['w', 19, 0], ['b', 14, 0], ['w', 23, 0], ['b', 17, 0]],
                  [['w', 17, 0], ['w', 19, 0], ['b', 14, 0], ['w', 22, 0]],
                   [['b', 8, 0], ['b', 10, 0], ['b', 11, 0], ['w', 18, 0]], # 5/6
                   [['w', 14, 0], ['w', 16, 0], ['w', 18, 0], ['w', 20, 0]], # 2/4
                   [['w', 17, 0], ['b', 13, 0], ['w', 21, 0], ['w', 23, 0]]], #5/4

            'G#':[[['b', 9, 0], ['w', 16, 0], ['b', 12, 0], ['b', 14, 0]],
             [['b', 10, 0], ['b', 11, 0], ['w', 19, 0], ['b', 14, 0]], 
             [['w', 16, 0], ['b', 12, 0], ['w', 20, 0], ['b', 15, 0]],
              [['b', 11, 0], ['w', 19, 0], ['b', 14, 0], ['b', 16, 0]], 
              [['b', 12, 0], ['w', 20, 0], ['b', 15, 0], ['b', 17, 0]],
               [['w', 19, 0], ['b', 14, 0], ['w', 23, 0], ['b', 17, 0]],
                [['w', 20, 0], ['b', 15, 0], ['w', 24, 0], ['w', 26, 0]],
                 [['w', 18, 0], ['w', 20, 0], ['b', 15, 0], ['b', 16, 0]],
                   [['b', 8, 0], ['b', 10, 0], ['b', 11, 0], ['w', 18, 0]], # 5/6
                   [['w', 14, 0], ['w', 16, 0], ['w', 18, 0], ['w', 20, 0]], # 2/4
                   [['w', 17, 0], ['b', 13, 0], ['w', 21, 0], ['w', 23, 0]]], #5/4

            'A#':[[['b', 5, 0], ['w', 10, 0], ['w', 12, 0], ['b', 10, 0]], 
            [['w', 9, 0], ['b', 7, 0], ['w', 13, 0], ['b', 10, 0]], 
            [['w', 10, 0], ['w', 12, 0], ['w', 14, 0], ['w', 16, 0]],
             [['b', 7, 0], ['w', 13, 0], ['b', 10, 0], ['b', 12, 0]],
              [['w', 12, 0], ['w', 14, 0], ['w', 16, 0], ['w', 19, 0]],
               [['w', 13, 0], ['b', 10, 0], ['w', 17, 0], ['w', 19, 0]], 
               [['w', 14, 0], ['w', 16, 0], ['w', 18, 0], ['w', 20, 0]],
                [['b', 8, 0], ['w', 14, 0], ['w', 16, 0], ['b', 12, 0]],
                   [['b', 8, 0], ['b', 10, 0], ['b', 11, 0], ['w', 18, 0]], # 5/6
                   [['w', 14, 0], ['w', 16, 0], ['w', 18, 0], ['w', 20, 0]], # 2/4
                   [['w', 17, 0], ['b', 13, 0], ['w', 21, 0], ['w', 23, 0]]], #5/4

            
}

piano_notes = ['A0', 'A0#', 'B0', 'C1', 'C1#', 'D1', 'D1#', 'E1', 'F1', 'F1#', 'G1', 'G1#',
               'A1', 'A1#', 'B1', 'C2', 'C2#', 'D2', 'D2#', 'E2', 'F2', 'F2#', 'G2', 'G2#',
               'A2', 'A2#', 'B2', 'C3', 'C3#', 'D3', 'D3#', 'E3', 'F3', 'F3#', 'G3', 'G3#',
               'A3', 'A3#', 'B3', 'C4', 'C4#', 'D4', 'D4#', 'E4', 'F4', 'F4#', 'G4', 'G4#',
               'A4', 'A4#', 'B4', 'C5', 'C5#', 'D5', 'D5#', 'E5', 'F5', 'F5#', 'G5', 'G5#',
               'A5', 'A5#', 'B5', 'C6', 'C6#', 'D6', 'D6#', 'E6', 'F6', 'F6#', 'G6', 'G6#',
               'A6', 'A6#', 'B6', 'C7', 'C7#', 'D7', 'D7#', 'E7', 'F7', 'F7#', 'G7', 'G7#',
               'A7', 'A7#', 'B7', 'C8']

white_notes = ['A0', 'B0', 'C1', 'D1', 'E1', 'F1', 'G1',
               'A1', 'B1', 'C2', 'D2', 'E2', 'F2', 'G2',
               'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3',
               'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4',
               'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5',
               'A5', 'B5', 'C6', 'D6', 'E6', 'F6', 'G6',
               'A6', 'B6', 'C7', 'D7', 'E7', 'F7', 'G7',
               'A7', 'B7', 'C8']

black_notes = ['Bb0', 'Db1', 'Eb1', 'Gb1', 'Ab1',
               'Bb1', 'Db2', 'Eb2', 'Gb2', 'Ab2',
               'Bb2', 'Db3', 'Eb3', 'Gb3', 'Ab3',
               'Bb3', 'Db4', 'Eb4', 'Gb4', 'Ab4',
               'Bb4', 'Db5', 'Eb5', 'Gb5', 'Ab5',
               'Bb5', 'Db6', 'Eb6', 'Gb6', 'Ab6',
               'Bb6', 'Db7', 'Eb7', 'Gb7', 'Ab7',
               'Bb7']

black_labels = ['A#0', 'C#1', 'D#1', 'F#1', 'G#1',
                'A#1', 'C#2', 'D#2', 'F#2', 'G#2',
                'A#2', 'C#3', 'D#3', 'F#3', 'G#3',
                'A#3', 'C#4', 'D#4', 'F#4', 'G#4',
                'A#4', 'C#5', 'D#5', 'F#5', 'G#5',
                'A#5', 'C#6', 'D#6', 'F#6', 'G#6',
                'A#6', 'C#7', 'D#7', 'F#7', 'G#7',
                'A#7']

chord_names = ['C', 'C7', 'Cmaj7', 'Cmaj9', 'Csus4', 'Cm', 'Cm7', 'Cmmaj7', 
          'C#', 'C#7', 'C#maj7', 'C#maj9', 'C#sus4', 'C#m', 'C#m7', 'C#mmaj7',
          'D', 'D7', 'Dmaj7', 'Dmaj9', 'Dsus4', 'Dm', 'Dm7', 'Dmmaj7', 
          'Db', 'Db7', 'Dbmaj7', 'Dbmaj9', 'Dbsus4', 'Dbm', 'Dbm7', 'Dbmmaj7', # = C# 1
          'D#', 'D#7', 'D#maj7', 'D#maj9', 'D#sus4', 'D#m', 'D#m7', 'D#mmaj7',
          'E', 'E7', 'Emaj7', 'Emaj9', 'Esus4', 'Em', 'Em7', 'Emmaj7', 
          'Eb', 'Eb7', 'Ebmaj7', 'Ebmaj9', 'Ebsus4', 'Ebm', 'Ebm7', 'ebmmaj7', # = D# 2
          'F', 'F7', 'Fmaj7', 'Fmaj9', 'Fsus4', 'Fm', 'Fm7', 'Fmmaj7', 
          'F#', 'F#7', 'F#maj7', 'F#maj9', 'F#sus4', 'F#m', 'F#m7', 'f#mmaj7',
          'G', 'G7', 'Gmaj7', 'Gmaj9', 'Gsus4', 'Gm', 'Gm7', 'Gmmaj7', 
          'Gb', 'Gb7', 'Gbmaj7', 'Gbmaj9', 'Gbsus4', 'Gbm', 'Gbm7', 'Gbmmaj7', # = F# 3
          'G#', 'G#7', 'G#maj7', 'G#maj9', 'G#sus4', 'G#m', 'G#m7', 'G#mmaj7',
          'A', 'A7', 'Amaj7', 'Amaj9', 'Asus4', 'Am', 'Am7', 'Ammaj7', 
          'Ab', 'Ab7', 'Abmaj7', 'Abmaj9', 'Absus4', 'Abm', 'Abm7', 'Abmmaj7', # = G# 4
          'A#', 'A#7', 'A#maj7', 'A#maj9', 'A#sus4', 'A#m', 'A#m7', 'A#mmaj7',
          'B', 'B7', 'Bmaj7', 'Bmaj9', 'Bsus4', 'Bm', 'Bm7', 'Bmmaj7', 
          'Bb', 'Bb7', 'Bbmaj7', 'Bbmaj9', 'Bbsus4', 'Bbm', 'Bbm7', 'Bbmmaj7',] # = A# 5

chord_sounds = []

scale_names = {'C' : ['C' ,'D', 'E', 'F', 'G', 'A', 'B', 'C'],
               'D': ['D', 'E', 'F#', 'G', 'A', 'B', 'C#', 'D'],
               'E': ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#', 'E'],
               'F': ['F', 'G', 'A,' 'Bb', 'C', 'D', 'E', 'F'],
               'G': ['G', 'A', 'B', 'C,' 'D', 'E', 'F#', 'G'],
               'A': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#', 'A'],
               'B': ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#', 'B'],
               'C#': ['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C,' 'Db'],
               'Db': ['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C,' 'Db'],
               'Eb': ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D', 'Eb'],
               'D#': ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D', 'Eb'],
               'Ab': ['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G', 'Ab'],
               'G#': ['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G', 'Ab'],
               'Bb': ['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'],
               'A#': ['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A', 'Bb']}

scale_sounds = {'C': [['w', 16, 5739], ['w', 17, 6108], ['w', 18, 6499], ['w', 19, 6935], ['w', 20, 7322], ['w', 21, 7738], ['w', 22, 8117], ['w', 23, 8554]],
          'D': [['w', 17, 1862], ['w', 18, 2290], ['b', 13, 2700], ['w', 20, 3079], ['w', 21, 3486], ['w', 22, 3839], ['b', 16, 4190], ['w', 24, 4589]],
          'E': [['w', 18, 1952], ['b', 13, 2326], ['b', 14, 2730], ['w', 21, 3139], ['w', 22, 3535], ['b', 16, 3895], ['b', 17, 4336], ['w', 25, 4732]],
          'F': [['w', 19, 1641], ['w', 20, 2045], ['w', 21, 2463], ['b', 15, 2843], ['w', 23, 3267], ['w', 24, 3680], ['w', 25, 4085], ['w', 26, 4456]],
          'G': [['w', 20, 14251], ['w', 21, 14675], ['w', 22, 15061], ['w', 23, 15421], ['w', 24, 15827], ['w', 25, 16203], ['b', 18, 16619], ['w', 27, 17005]],
          'A': [['w', 21, 1538], ['w', 22, 1912], ['b', 16, 2279], ['w', 24, 2641], ['w', 25, 2997], ['b', 18, 3348], ['b', 19, 3722], ['w', 28, 4112]],
          'B': [['w', 22, 1809], ['b', 16, 2144], ['b', 17, 2501], ['w', 25, 2849], ['b', 18, 3173], ['b', 19, 3560], ['b', 20, 3913], ['w', 29, 4261]],
          'C#': [['b', 11, 2318], ['b', 12, 2721], ['w', 19, 3183], ['b', 13, 3679], ['b', 14, 4194], ['b', 15, 4648], ['w', 23, 5149], ['b', 16, 5589]],
          'Db': [['b', 11, 2318], ['b', 12, 2721], ['w', 19, 3183], ['b', 13, 3679], ['b', 14, 4194], ['b', 15, 4648], ['w', 23, 5149], ['b', 16, 5589]],
          'D#': [['b', 12, 4150], ['w', 19, 4602], ['w', 20, 5026], ['b', 14, 5393], ['b', 15, 5783], ['w', 23, 6173], ['w', 24, 6677], ['b', 17, 7109]],
          'Eb': [['b', 12, 4150], ['w', 19, 4602], ['w', 20, 5026], ['b', 14, 5393], ['b', 15, 5783], ['w', 23, 6173], ['w', 24, 6677], ['b', 17, 7109]],
          'F#': [['b', 13, 1191], ['b', 14, 1592], ['b', 15, 1996], ['w', 22, 2430], ['b', 16, 2817], ['b', 17, 3256], ['w', 26, 3713], ['b', 18, 4109]],
          'Ab': [['b', 14, 1746], ['b', 15, 2141], ['w', 23, 2573], ['b', 16, 2956], ['b', 17, 3398], ['w', 26, 3838], ['w', 27, 4251], ['b', 19, 4611]],
          'G#': [['b', 14, 1746], ['b', 15, 2141], ['w', 23, 2573], ['b', 16, 2956], ['b', 17, 3398], ['w', 26, 3838], ['w', 27, 4251], ['b', 19, 4611]],
          'A#': [['b', 15, 2679], ['w', 23, 3102], ['w', 24, 3496], ['b', 17, 3872], ['w', 26, 4283], ['w', 27, 4664], ['w', 28, 5021], ['b', 20, 5406]],
          'Bb': [['b', 15, 2679], ['w', 23, 3102], ['w', 24, 3496], ['b', 17, 3872], ['w', 26, 4283], ['w', 27, 4664], ['w', 28, 5021], ['b', 20, 5406]],}