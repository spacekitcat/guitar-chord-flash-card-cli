import sys
import random
import inquirer


def render_fret_seperator(character, guitar_string_count):
  fret_character_count = (guitar_string_count * 2) - 1 
  for i in range(fret_character_count):
    sys.stdout.write(character)
  sys.stdout.write('\n')

def render_fret_section(fret, guitar_string_count):
  for i in range(0, guitar_string_count):
    guitar_string = guitar_string_count - i
    if guitar_string in fret:
      sys.stdout.write('O ')
    else:
      sys.stdout.write('| ')
  sys.stdout.write('\n')


def get_chords():
  return {
    'a_major': {
      'frets': [
        [],
        [2, 3, 4],
        [],
      ],
    },
    'c_major': {
      'frets': [
        [2],
        [4],
        [5],
      ]
    },
    'd_major': {
      'frets': [
        [],
        [1, 3],
        [2],
      ]
    },
    'g_major': {
      'frets': [
        [],
        [5],
        [1, 6],
      ]
    },
    'e_major': {
      'frets': [
        [3],
        [4, 5]
      ]
    },
    'e_minor': {
      'frets': [
        [],
        [4, 5]
      ]
    },
    'd_minor': {
      'frets': [
        [1],
        [3],
        [2]
      ]
    },
    'a_minor': {
      'frets': [
        [2],
        [3, 4],
      ]
    },
  }


def render_chord(chord, guitar_string_count):
    render_fret_seperator('=', guitar_string_count)
    for fret in chord:
      render_fret_section([], guitar_string_count)
      render_fret_section(fret, guitar_string_count)
      render_fret_section([], guitar_string_count)
      render_fret_seperator('-', guitar_string_count)


def show_quiz_prompt(chords, current_question, current_question_number):
  questions = [
    inquirer.List(
      'chord',
      message=f'[{current_question}/{current_question_number}] What chord is this?',
      choices=list(chords.keys())
    ),
  ]

  answers = inquirer.prompt(questions)
  return answers['chord']

def main():
  quiz_question_count = 10
  correct_answer_count = 0
  chord_map = get_chords()
  guitar_string_count = 6

  for i in range(quiz_question_count):
    random_chord_key = random.choice(list(chord_map.keys()))
    if random_chord_key in chord_map:
      render_chord(chord_map[random_chord_key]['frets'], guitar_string_count)
      current_question_number = i+1
    
      if show_quiz_prompt(chord_map, current_question_number, quiz_question_count) == random_chord_key:
        correct_answer_count += 1
        input(f'Correct. This is {random_chord_key} (press any key to continue)')
      else:
        input(f'Incorrect. This is {random_chord_key} (press any key to continue)')
      sys.stdout.write('\n')

    else:
      sys.stdout.write(f'No chord data found for key "{random_chord_key}" \n')

  sys.stdout.write(f'Score: {correct_answer_count} / {quiz_question_count} ({correct_answer_count / quiz_question_count * 100}%)\n\n')

if __name__ == '__main__':
  main()
