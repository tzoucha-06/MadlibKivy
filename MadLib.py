import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView

# Set the window size for better appearance
Window.size = (600, 800)


class MadLibsWidget(BoxLayout):
    """Main widget containing the Mad Libs game interface"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        # Create and add a title label
        title_label = Label(text='Mad Libs Game', font_size=24, size_hint_y=None, height=40)
        self.add_widget(title_label)

        # Create input container
        input_layout = BoxLayout(orientation='vertical', spacing=5, size_hint_y=0.5)

        # Create labeled inputs for noun, verb, and adjective
        self.noun_input = self._create_labeled_input(input_layout, "Noun:", "Enter a noun")
        self.verb_input = self._create_labeled_input(input_layout, "Verb:", "Enter a verb")
        self.adj_input = self._create_labeled_input(input_layout, "Adjective:", "Enter an adjective")

        # Add input_layout to the main widget
        self.add_widget(input_layout)

        # Create control section
        control_layout = BoxLayout(size_hint_y=0.2, spacing=10)

        # Create and add Spinner for mood selection
        self.mood_spinner = Spinner(
            text='Choose mood',
            values=('Happy', 'Sad', 'Excited', 'Angry', 'Nervous'),
            size_hint_x=0.4
        )
        control_layout.add_widget(self.mood_spinner)

        # Create and add Button to generate story
        self.generate_btn = Button(
            text='Generate Story!',
            size_hint_x=0.4
        )
        self.generate_btn.bind(on_press=self.generate_story)
        control_layout.add_widget(self.generate_btn)

        # Create and add Button to reset inputs
        self.reset_btn = Button(
            text='Reset',
            size_hint_x=0.4
        )
        self.reset_btn.bind(on_press=self.reset_inputs)
        control_layout.add_widget(self.reset_btn)

        # Create and add Button to show help
        self.help_btn = Button(
            text='Help',
            size_hint_x=0.4
        )
        self.help_btn.bind(on_press=self.show_help)
        control_layout.add_widget(self.help_btn)

        # Add control_layout to main widget
        self.add_widget(control_layout)

        # Create and add a scrollable story display Label
        self.story_label = Label(
            text='Your story will appear here!',
            size_hint_y=None,
            height=100,
            halign='center',
            valign='middle'
        )
        self.story_label.bind(size=self.story_label.setter('text_size'))  # Allow text wrapping

        # Wrap the story label in a ScrollView for better usability
        scroll_view = ScrollView(size_hint_y=0.3)
        scroll_view.add_widget(self.story_label)
        self.add_widget(scroll_view)

        # Predefined lists for random story generation
        self.nouns = ["cat", "dog", "car", "house", "tree"]
        self.verbs = ["run", "jump", "swim", "fly", "dance"]
        self.adjectives = ["happy", "sad", "excited", "angry", "funny"]
        self.moods = ["Happy", "Sad", "Excited", "Angry", "Nervous"]

        # Predefined story templates
        self.story_templates = [
            "The {adj} {noun} decided to {verb} because it was feeling {mood}.",
            "Once upon a time, a {adj} {noun} wanted to {verb} while feeling {mood}.",
            "In a {adj} world, a {noun} chose to {verb} because it was {mood}.",
            "A {noun} that was {adj} wanted to {verb} to express its {mood} feelings.",
            "The {adj} {noun} and its friend decided to {verb} together, feeling very {mood}.",
            "On a {adj} day, a {noun} wanted to {verb} to show its {mood} side.",
            "In a magical land, a {noun} that was {adj} decided to {verb} because it felt {mood}.",
            "A {adj} {noun} went on an adventure to {verb} and spread {mood} vibes everywhere."
        ]

    def _create_labeled_input(self, layout, label_text, hint_text):
        label = Label(text=label_text)
        text_input = TextInput(hint_text=hint_text, multiline=False)
        layout.add_widget(label)
        layout.add_widget(text_input)
        return text_input

    def generate_story(self, instance):
        # Get input values or randomly select if inputs are empty
        noun = self.noun_input.text.strip() or random.choice(self.nouns)
        verb = self.verb_input.text.strip() or random.choice(self.verbs)
        adj = self.adj_input.text.strip() or random.choice(self.adjectives)
        mood = self.mood_spinner.text if self.mood_spinner.text != 'Choose mood' else random.choice(self.moods)

        # Generate a random story template
        story_template = random.choice(self.story_templates)

        # Generate story
        story = story_template.format(adj=adj, noun=noun, verb=verb, mood=mood)
        self.story_label.text = story

    def reset_inputs(self, instance):
        """Reset all input fields and the story display"""
        self.noun_input.text = ''
        self.verb_input.text = ''
        self.adj_input.text = ''
        self.mood_spinner.text = 'Choose mood'
        self.story_label.text = 'Your story will appear here!'

    def show_help(self, instance):
        help_message = (
            "Welcome to the Mad Libs Game!\n\n"
            "1. Enter a noun, verb, and adjective in the respective fields.\n"
            "2. Choose a mood from the dropdown menu.\n"
            "3. Click 'Generate Story!' to create a fun story.\n"
            "4. Use 'Reset' to clear the inputs and start over.\n"
            "5. Click 'Help' for this message."
        )
        self.show_popup("Help", help_message)

    def show_popup(self, title, message):
        """Show a popup message"""
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.8, 0.4))
        popup.open()


class MadLibsApp(App):
    """Main application class"""
    def build(self):
        return MadLibsWidget()


if __name__ == '__main__':
    MadLibsApp().run()
