import reflex as rx
import os
import datetime
from .options import OptionsState
from anthropic import AsyncAnthropic

from dotenv import load_dotenv

load_dotenv()
ANTHROPIC_API_KEY = os.getenv("API_KEY_ANTHROPIC")
client = AsyncAnthropic(api_key=ANTHROPIC_API_KEY)

CopyLocalState = rx._x.client_state(default=False, var_name="copying")


class SummaryState(rx.State):
    generated_text: str = None

    @rx.background
    async def generate_text(self):
        try:
            # Check if the env variable is set
            if not self._check_api_key():
                return
            async with self:
                Options = await self.get_state(OptionsState)
            # If prompt is empty
            if Options.text == "":
                yield rx.toast.warning("Please enter a prompt")
                return
            input = {
                "text": Options.text,
                "summary_length": Options.summary_length,
            }
            print(f"input: {input}")

            message = await client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=500,
                system="You are a text summarizer. You will be given a text and you will need to summarize it. Only send the summary, no other text (don't the word 'summary' in your response. Don't respond as your were a third person, instead use the person who is summarizing the text.",
                messages=[
                    {
                        "role": "user",
                        "content": f"Create a short summarize of this text: {input['text']}. Limit the summary to {input['summary_length']} words.",
                    }
                ],
            )
            response = message.content[0].text
            async with self:
                self.generated_text = response
            print(f"Response: {response}")

        except Exception as e:
            async with self:
                self.generated_text = str(e)
                self._reset_state()
            yield rx.toast.error(f"Error, please try again: {e}")

    def _reset_state(self):
        self.generated_text = None

    def _check_api_key(self):
        if os.getenv(ANTHROPIC_API_KEY) is None:
            yield rx.toast.warning("No API key found")
            return False
        return True

    @rx.background
    async def download_text(self):
        async with self:
            Options = await self.get_state(OptionsState)
        filename = (
            f"reflex_ai_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        )
        print(f"filename: {filename}")
        try:

            content = f"""Input Text:
{Options.text}

Summary Length: {Options.summary_length} words

Generated Summary:
{self.generated_text}"""

            print(f"content: {content}")

            yield rx.download(data=content, filename=filename)

        except Exception as e:
            yield rx.toast.error(f"Error downloading text: {e}")

    async def copy_text(self):
        try:
            yield rx.set_clipboard(self.generated_text)
        except Exception as e:
            yield rx.toast.error(f"Error copying generated text: {e}")


def copy_script():
    return rx.call_script(
        """
        refs['_client_state_setCopying'](true);
        setTimeout(() => {
            refs['_client_state_setCopying'](false);
        }, 1750);
        """
    )
