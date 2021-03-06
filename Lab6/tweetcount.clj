(ns tweetcount
    (:use     [streamparse.specs])
    (:gen-class))

(defn tweetcount [options]
  [
    ;; spout configuration
    {"sentence-spout" (python-spout-spec
        options
            "spouts.sentences.Sentences"
            ["sentence"]
            )
    }
    ;; Bolts
    {
        ;; bolt configuration 1
        "parse-bolt" (python-bolt-spec
          options
          {"sentence-spout" :shuffle}
          "bolts.parse.ParseTweet"
          ["valid_words"]
          :p 2
          )
        ;; bolt configuration 2
        "tweetcounter-bolt" (python-bolt-spec
          options
          {"parse-bolt" ["valid_words"]}
          "bolts.tweetcounter.TweetCounter"
          ["word", "counts"]
          :p 1
          )
    }
  ]
)
