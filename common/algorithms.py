from itertools import combinations
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text

from .categories import Categories


class Algorithms:
    duplicate_model: tf.keras.Model = tf.keras.models.load_model(
        "models/duplicates.keras", custom_objects={"KerasLayer": hub.KerasLayer}
    )
    classification_model: tf.keras.Model = tf.keras.models.load_model(
        "models/classification.keras", custom_objects={"KerasLayer": hub.KerasLayer}
    )

    @classmethod
    def detect_duplicates(cls, text_list: list[str]) -> list[list[str]]:
        texts_combinations = combinations(text_list, 2)
        predictions = cls.duplicate_model.predict(
            tf.data.Dataset.from_tensor_slices(
                {
                    key: value
                    for key, value in zip(
                        ["text_1", "text_2"], map(list, zip(*texts_combinations))
                    )
                }
            ).batch(64),
            batch_size=64,
            verbose=0,
        )[:, 0]

        duplicate_groups: list[set[str]] = []

        for prediction, (first_text, second_text) in zip(
            predictions, texts_combinations
        ):
            if prediction < 0.5:
                continue
            for group in duplicate_groups:
                if first_text in group or second_text in group:
                    group.add(first_text)
                    group.add(second_text)
                    break
            else:
                duplicate_groups.append({first_text, second_text})

        return list(map(list, duplicate_groups))

    def match_pair(self, first: str, second: str) -> bool:
        return False

    @classmethod
    def classify_category(cls, text: str | list[str]) -> list[Categories]:
        if isinstance(text, str):
            text = [text]

        predictions = cls.classification_model.predict(text, batch_size=64, verbose=0)
        labels = predictions.argmax(1)

        return list(map(Categories, labels))
