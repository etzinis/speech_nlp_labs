#===================================LAB 2 KALDI SPEECH RECOGNITION===================================================

. ./cmd.sh

#wsj0=/home/patrec/kaldi-trunk/egs/wsj/s5/WSJ0_2015   

#local/wsj_data_prep.sh $wsj0/??-{?,??}.? $wsj0/??-{?,??}.?  || exit 1;

#local/wsj_prepare_dict.sh --dict-suffix "_nosp" || exit 1;
#bash ./utils/prepare_lang.sh data/local/dict_nosp \
#  "<SPOKEN_NOISE>" data/local/lang_tmp_nosp data/lang_nosp || exit 1;

#local/wsj_format_data.sh --lang-suffix "_nosp" || exit 1;


#===============================Make the mfcc===========================================================================
# Now make MFCC features.
# mfccdir should be some place with a largish disk where you
# want to store MFCC features.

#mfccdir=mfcc
#for x in train_si84 test_eval92 test_eval92_5k; do 
# steps/make_mfcc.sh --cmd "$train_cmd" --nj 20 \
#   data/$x exp/make_mfcc/$x $mfccdir || exit 1;
# steps/compute_cmvn_stats.sh data/$x exp/make_mfcc/$x $mfccdir || exit 1;
#done

#=============================-=====================Make the division====================================================

# Now make subset with the shortest 2k utterances from si-84.
#utils/subset_data_dir.sh --shortest data/train_si84 1806 data/train_si84_2kshort || exit 1;

# Now make subset with half of the data from si-84.
#utils/subset_data_dir.sh data/train_si84 1806 data/train_si84_half || exit 1;

#===================================Make the training=================================================================
# Note: the --boost-silence option should probably be omitted by default
# for normal setups.  It doesnt always help. [its to discourage non-silence
# models from modeling silence.]
#steps/train_mono.sh --boost-silence 1.25 --nj 3 --cmd "$train_cmd" \
#  data/train_si84_2kshort data/lang_nosp exp/mono0a || exit 1;

#(
#utils/mkgraph.sh --mono data/lang_nosp_test_tgpr \
#   exp/mono0a exp/mono0a/graph_nosp_tgpr && \
# steps/decode.sh --nj 3 --cmd "$decode_cmd" exp/mono0a/graph_nosp_tgpr \
#   data/test_dev93 exp/mono0a/decode_nosp_tgpr_dev93 && \
# steps/decode.sh --nj 2 --cmd "$decode_cmd" exp/mono0a/graph_nosp_tgpr \
#   data/test_eval92 exp/mono0a/decode_nosp_tgpr_eval92 
#) &

#steps/align_si.sh --boost-silence 1.25 --nj 3 --cmd "$train_cmd" \
#  data/train_si84_half data/lang_nosp exp/mono0a exp/mono0a_ali || exit 1;

#steps/train_deltas.sh --boost-silence 1.25 --cmd "$train_cmd" 2000 10000 \
#  data/train_si84_half data/lang_nosp exp/mono0a_ali exp/tri1 || exit 1;

#while [ ! -f data/lang_nosp_test_tgpr/tmp/LG.fst ] || \
#   [ -z data/lang_nosp_test_tgpr/tmp/LG.fst ]; do
#  sleep 20;
#done
#sleep 30
#==============================================================================================================


#=============Make the testing for out trained model========================================================

#utils/mkgraph.sh data/lang_nosp_test_tgpr \
# exp/tri1 exp/tri1/graph_nosp_tgpr || exit 1;

#steps/decode.sh --nj 2 --cmd "$decode_cmd" exp/tri1/graph_nosp_tgpr \
#  data/test_eval92 exp/tri1/decode_nosp_tgpr_eval92 || exit 1;

#===========================================================================================================

#======================Printing the best WER Result=====================================================

# for x in exp/*/decode*; do [ -d $x ] && grep WER $x/wer_* | utils/best_wer.sh; done

#=========================================================================================================
