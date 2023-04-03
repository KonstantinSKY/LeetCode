"""1160. Find Words That Can Be Formed by Characters https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/ """

import time
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        for word in words:
            flag = 1
            for char in word:
                if chars.count(char) < word.count(char):
                    flag = 0
                    break
            if flag:
                count += len(word)
        return count

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().countCharacters(["cat", "bt", "hat", "tree"], "atach"))
    print(Solution().countCharacters(
        ["dyiclysmffuhibgfvapygkorkqllqlvokosagyelotobicwcmebnpznjbirzrzsrtzjxhsfpiwyfhzyonmuabtlwin",
         "ndqeyhhcquplmznwslewjzuyfgklssvkqxmqjpwhrshycmvrb", "ulrrbpspyudncdlbkxkrqpivfftrggemkpyjl", "boygirdlggnh",
         "xmqohbyqwagkjzpyawsydmdaattthmuvjbzwpyopyafphx",
         "nulvimegcsiwvhwuiyednoxpugfeimnnyeoczuzxgxbqjvegcxeqnjbwnbvowastqhojepisusvsidhqmszbrnynkyop",
         "hiefuovybkpgzygprmndrkyspoiyapdwkxebgsmodhzpx",
         "juldqdzeskpffaoqcyyxiqqowsalqumddcufhouhrskozhlmobiwzxnhdkidr",
         "lnnvsdcrvzfmrvurucrzlfyigcycffpiuoo", "oxgaskztzroxuntiwlfyufddl",
         "tfspedteabxatkaypitjfkhkkigdwdkctqbczcugripkgcyfezpuklfqfcsccboarbfbjfrkxp",
         "qnagrpfzlyrouolqquytwnwnsqnmuzphne",
         "eeilfdaookieawrrbvtnqfzcricvhpiv", "sisvsjzyrbdsjcwwygdnxcjhzhsxhpceqz",
         "yhouqhjevqxtecomahbwoptzlkyvjexhzcbccusbjjdgcfzlkoqwiwue",
         "hwxxighzvceaplsycajkhynkhzkwkouszwaiuzqcleyflqrxgjsvlegvupzqijbornbfwpefhxekgpuvgiyeudhncv",
         "cpwcjwgbcquirnsazumgjjcltitmeyfaudbnbqhflvecjsupjmgwfbjo", "teyygdmmyadppuopvqdodaczob",
         "qaeowuwqsqffvibrtxnjnzvzuuonrkwpysyxvkijemmpdmtnqx"],
        "usdruypficfbpfbivlrhutcgvyjenlxzeovdyjtgvvfdjzcmikjraspdfp"))
    print(Solution().countCharacters(["pxlqovnbsgvqjzpfeidchzrodnbqfrccfydzjptukscjuatlsrcurepllxzyghhdepitqptlmfkhzxjgswaulxkfydhkilg",
                                      "uqklvqnlhdkwryjawkqfajfpbcnhglxlwxlaskxlytr","jvgkxcdkxrvfahjkvhmfuyjzxtyxrsogbtsjybeaxugqymcr",
                                      "rgxditmosplnqvodtis","jm","ruqjwejuanjtiizcmbieobesnjnadzqvqumggblzmkxilgfarnxwpcawtkzxlvugibpidvwtikloeziuxqoi",
                                      "wxeyzrnbhlhwxecrgejsrawyulynvgtszwqqlihkcvckgcgtgpyqtkuwvjywmhpskaiwmpyarftqhnogxpith",
                                      "vdpbykqlihtpvfnqbrcjpggojqbalerohyitktuikbffvfatcnneuvbanjihiaorrjcdthntnrxebfhvshmpodmzhtwnasbm",
                                      "wgjstkoaojcesfdrllugmojwdmgeejyiqvshlowtktddattunarnohgvqsoskfmbrami","ecwqxbawirvnxvsjybbebclaturorlcbpf",
                                      "gtjbaigvufrotlwfoqqolnjabnvtbcygtfcytinzpcjbvprdkdjawrcbthmxjrabimhhs",
                                      "cvzlbrvppkyxtjxzeglzwoagmpjnfxddbwolxmwdohgtfktgftzzkwpianslkpldyfzubtjczse","neaw",
                                      "mxhmvkajofnmdiiduactlemcvpztscmsnrdhuhquxnnzywsrzxyplgbppiypxwcfbsnyzblaeifo",
                                      "krekecabfpufucjhqphjnibaeqdvdpmrfougdwugvoioqangdnxromwlxnfeydaneyazzclscqgdxlhhgnoqmslfflzqv",
                                      "klutvchxsceihfmzitgqakytesfjykribjhjzdruuoycjkwaghmmqkfrhkrtawudtjyjwqbyspamlegqjlwlj",
                                      "raykfkflqdzrpthdejetwolgciygwaktulkxemkdbbllkjxhnnafsms","os",
                                      "xhchkcetmlprcdmrnalvkvgabxxnomphqpqhnddqhecogspbdebeoshvjgzvmqu",
                                      "jqtdysnpskktynxwmsfaabglagnqcllptvuyyqjwrmqaftenusmsahhhqubkwxltpr",
                                      "sulmwluiwvlroldpiyecaicwrawzwflokefqkdwmxejaovvpbflfdtviinbvvtlhhhefmgfsqs","sxyhcckvyl",
                                      "vsaacsybcddxvuzkddjmuivsvtjyanpbydmkcwnkmxvsiantgkvkmqjysclsvd","sxcghypulvmfqfunxj","pozekufhlooosxpcggbi",
                                      "xzaoxzllcixfqbupqozmzrnugj","j","tgslwp","ntrdkixexajlpjgmcbrqimwtqnzfrqjszeiuvrgzclerzmsnagzaxbredvlrmipzflrzusclckmxphc",
                                      "ifdflsywdfizpodsehrrifsvejcxarrxmxyjgbbvqyqvywncphzfmnxhybxpdcozfnzablfx",
                                      "uluhplzrsaehaqxfnbcmixueedevhirbwqdyztwaxnkogcauymxgcpabxekib","agtfkinbdccoemxetbryzpluzlpyzicnfopphrxriqm",
                                      "pdympxpwvxwcqaxrvbvyqkrresrjgzgxuyfxtkgldtathokdbyfsqfmitmiyagtqgijaiazvsumeyutbbwxqdshquzrehn","rqe","sljsvenhhstnnngzqyo",
                                      "dezrzpgldeimxfoqajuhjctgvalwkhkjemjaxumxqmifglbizusuqlttxirpbqbuvauwy",
                                      "dkwpyezbmkcskoxxcgrxcewknqgdckjxfyzcmzqcbyeucxbqybxoldogtkmdknsrruvnlfqnpfx",
                                      "sjeftmjkuperfynbreycwhuoyqybticswblbrrpugzhlrmiedjqufnehevzqwtaebwvdswsz",
                                      "lolnfyliloqmhjmhhohdtgfajjfdjqpubslbsrwitbjmrcegdrdjzvonxaefdvdfcbqmaaks","qhcoaiocjhuzywkirlblajgeapzajqsoa",
                                      "sxrmoqxqbtakuqwmrrkljmegbwbeqbywmlyuprwyhljzejbybxoumidpxdrohwdjoqycpxcmivaulnqzneydwqfsvcxgyyseuk","yrowy",
                                      "dohrzkrzdjehpctnjrvhzojullsiucrhphshwxwicyzkvzbqrztic",
                                      "rmshnxtbhsdgkiijrmwulocdzjzpgfyimkjdthuzkhoqgkeawgwincubrloknocxwzgqqcxafksxgzh",
                                      "aymovnuhptozhkiyowbeguzlkmrwjnujgjbdne","abc","vxoigovwmqizmkwbkktqk",
                                      "uokwktdempzloaglvvkqstztmwzcmhgxtoua","bzwjxqueazlzfojrkbqmhtwrvuwsnfcnylurnddpektekca",
                                      "qgndjgvzcyajhgmrrnhdywwdbmkhtthwcfiueuxfldanyrmccwcy"],"figspbov"))


    print("--- %s seconds ---" % (time.time() - start_time))
