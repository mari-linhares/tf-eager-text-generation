# Import TensorFlow >= 1.10 and enable eager execution
import tensorflow as tf
# Note: Once you enable eager execution, it cannot be disabled. 
tf.enable_eager_execution()

import datasources
import models
from learning.trainer import Trainer

from utils.args import parser


def main():
    args = parser.parse_args()
    ds = datasources.load(args.text_path, ds_name=args.text_type,
                          max_length=args.max_length,
                          buffer_size=args.buffer_size,
                          batch_size=args.batch_size,
                          to_lower=args.to_lower)

    model = models.load(ds.vocab_size, embedding_dim=args.embedding_dim, units=args.units)
    trainer = Trainer(datasource=ds, model=model, optimizer=tf.train.AdamOptimizer(),
                      checkpoint_dir=args.checkpoint_dir, checkpoint_prefix=args.checkpoint_prefix)

    trainer.train(epochs=args.epochs, verbose=args.verbose)

if __name__ == '__main__':
    main()