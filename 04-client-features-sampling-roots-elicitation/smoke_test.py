"""Smoke test for Lesson 04: the exchange covers every feature."""
import features_twin

def main():
    text = " ".join(m + n for _, m, n in features_twin.EXCHANGE)
    for needle in ["elicitation/create", "notifications/progress",
                   "notifications/message", "sampling/createMessage",
                   "roots/list_changed", "progressToken"]:
        assert needle in text, needle
    print("smoke ok: elicitation, progress, logging, sampling, roots all present")

if __name__ == "__main__":
    main()
