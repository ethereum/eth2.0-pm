# Ethereum 2.0 Implementers Call 21 Notes

## Contents


- [Contents](#contents)
- [1 Meeting Details](#1-meeting-details)
- [2 Attendees](#2-attendees)
- [3 Agenda](#3-agenda)
	- [3.1 Testing Updates](#31-testing-updateshttpsyoutubeyb8o5qjnbct245)
		- [3.1.1 Overflow in Slashing](#311-overflow-in-slashinghttpsgithubcomethereumeth20-specspull1286)
		- [3.1.2 Spec Freeze](#312-spec-freezehttpsgithubcomethereumeth20-specspull1242)
		- [3.1.3 Fuzzing](#313-fuzzinghttpsgithubcomethereumeth20-specstreedevtestlibspyspeceth2specfuzzing)
	- [3.2 Client Updates](#32-client-updateshttpsyoutubeyb8o5qjnbct830)
		- [3.2.1 Nimbus](#321-nimbushttpsgithubcomstatus-imnimbus)
		- [3.2.2 Artemis](#322-artemishttpsgithubcompegasysengartemis)
		- [3.2.3 Trinity](#323-trinityhttpsgithubcomethereumtrinity)
		- [3.2.4 Yeeth](#324-yeethhttpsgithubcomyeeth)
		- [3.2.5 Harmony](#325-harmonyhttpsdocsethhubioethereum-roadmapethereum-20eth20-teamsharmony)
		- [3.2.6 Lighthouse](#326-lighthousehttpsgithubcomsigplighthouse)
		- [3.2.7 Prysmatic](#327-prysmatichttpsgithubcomprysmaticlabs)
		- [3.2.8 Lodestar](#328-lodestarhttpsgithubcomchainsafelodestar)
		- [3.2.9 Parity](#329-parityhttpsgithubcomparitytechparity-ethereum)
	- [3.3 Research Updates](#33-research-updateshttpsyoutubeyb8o5qjnbct1725)
		- [3.3.1 Phase 0](#331-phase-0httpsdocsethhubioethereum-roadmapethereum-20eth-20-phases)
		- [3.3.2 Phase 1](#332-phase-1httpsdocsethhubioethereum-roadmapethereum-20eth-20-phases)
		- [3.3.3 Phase 2](#333-phase-2httpsdocsethhubioethereum-roadmapethereum-20eth-20-phases)
		- [3.3.4 PegaSys](#334-pegasyshttpsgithubcompegasyseng)
		- [3.3.5 Runtime Verification](#335-runtime-verificationhttpsgithubcomruntimeverificationalgorand-verification)
	- [3.4 Network](#34-networkhttpsyoutubeyb8o5qjnbct2470)
		- [3.4.1 Libp2p](#341-libp2phttpsgithubcomlibp2pjs-libp2p)
		- [3.4.2 Gossiping Mechanism and Episub](#342-gossiping-mechanism-and-episubhttpsgithubcomlibp2pspecsblobmasterpubsubgossipsubepisubmdartemis-prysmatic-labs-lodestar-handles-exchange)
	- [3.5 Spec Discussion](#35-spec-discussionhttpsyoutubeyb8o5qjnbct5095)
	- [3.6 Open Discussion/Closing Remarks](#36-open-discussionclosing-remarkshttpsyoutubeyb8o5qjnbct5540)



## 1 Meeting Details

- **Meeting Date-Time:** Thursday 2019/7/11 at [14:00 GMT](http://www.timebie.com/std/gmt.php?q=14)
- **Meeting Duration:** 1.5 hours
- **[Youtube Livestream](https://www.youtube.com/watch?v=YB8o_5qjNBc)**

## 2 Attendees

- [Adrian Manning](https://github.com/AgeManning)
- [Alex Stokes](https://github.com/ralexstokes)
- [Ben Edgington](https://github.com/benjaminion)
- [Benjamin Burns](https://github.com/benjamincburns)
- [Carl Beekhuizen](https://github.com/CarlBeek)
- [Cem Ozer](https://github.com/cemozerr)
- [Daniel Ellison](https://github.com/zigguratt)
- [Dankrad Feist](https://github.com/dankrad)
- [Danny Ryan](https://github.com/djrtwo)
- [Dean Eigenmann](https://github.com/decanus)
- [Diederik Loerakker](https://github.com/protolambda)
- [Dmitriy Ryajov](https://github.com/dryajov)
- [Greg Markou](https://github.com/GregTheGreek)
- [Hsiao-Wei Wang](https://github.com/hwwhww)
- [Jacek Sieka](https://github.com/arnetheduck)
- [Jannik Luhn](https://github.com/jannikluhn)
- [John Adler](https://media.consensys.net/@adlerjohn)
- [Jonny Rhea](https://github.com/jrhea)
- JosephC
- [Joseph Delong](https://github.com/dangerousfood)
- [Justin Drake](https://github.com/JustinDrake)
- [Kevin Main-Hsuan Chia](https://github.com/mhchia)
- [Leo Bautista Gomez](https://github.com/leobago)
- [Luke Anderson](https://github.com/spble)
- [Mamy Ratsimbazafy](https://github.com/mratsim)
- [Matt Garnett](https://github.com/c-o-l-o-r)
- [Mike Goelzer](https://github.com/mgoelzer)
- [Mikhail Kalinin](https://github.com/mkalinin)
- [Musab Alturki](https://github.com/malturki)
- [Nicholas Lin](https://www.linkedin.com/in/nicholas-lin-50267ba3/)
- [Nicolas Liochon](https://github.com/nkeywal)
- [Paul Hauner](https://github.com/paulhauner)
- [Preston](https://github.com/prestonvanloon)
- [Raul Jordan](https://github.com/rauljordan)
- [Raúl Kripalani](https://github.com/raulk)
- [Steven Schroeder](https://github.com/schroedingerscode)
- [Trenton Van Epps](https://medium.com/@trenton.v)
- [Vitalik Buterin](https://vitalik.ca/)
- [Wei Tang](https://github.com/sorpaas)
- [Whiteblock](https://github.com/Whiteblock)
- [Will Villanueva](https://medium.com/@william.j.villanueva)
- [Zak Cole](https://github.com/zscole)

## 3 Agenda

### 3.1 [Testing Updates](https://youtu.be/YB8o_5qjNBc?t=245)


#### 3.1.1 [Overflow in Slashing](https://github.com/ethereum/eth2.0-specs/pull/1286)

**Timestamp: [4:06](https://youtu.be/YB8o_5qjNBc?t=245)**

**Danny Ryan**: Prysmatic Labs, Terence [Tsao], found an issue where the calculation and slashing was, due to the way it was formatted, potentially overflowing in a tester for `uint64`

Relatively non-substantive changes (fixes, documentation, and things) in v08x branch [#1286](https://github.com/ethereum/eth2.0-specs/pull/1286). Includes a fix to this which alters the way the computation happens. Non-substantive, but doesn't overflow. Seems relatively important so will get out v08x in the next few days (includes other minor things people have found).

#### 3.1.2 [Spec Freeze](https://github.com/ethereum/eth2.0-specs/pull/1242)

**Timestamp: [5:12](https://youtu.be/YB8o_5qjNBc?t=309)**

**Diederik Loerakker**: Spec Freeze is over now, can stop throwing up to the spec and build.

**Danny Ryan**: Even after the Spec Freeze we will be expanding the coverage of the tests as needed.

#### 3.1.3 [Fuzzing](https://github.com/ethereum/eth2.0-specs/tree/dev/test_libs/pyspec/eth2spec/fuzzing)

**Timestamp: [6:51](https://youtu.be/YB8o_5qjNBc?t=411)**


**Justin Drake**: Goal: Basic Fuzzing infrastructure for all the clients.
  * Client implementers don't have to worry too much about being compliant with the State Transition Function.
  * You can spend most of your time on what makes a client "a client": Networking, Databases, and what-not.

We've started with pySpec and the goal executable specs. I think the next target for integration will be Lighthouse. Hopefully, a lot of the infrastructure will be generic for clients. Might come in the next two weeks, hopefully.

**Danny Ryan**: We'll go the experiment round with one and learn some things.

**Diederik Loerakker**: We are Fuzzing v0.8.0 and Go excludes post-spec is almost up-to-date now, pySpec already is. It's really up to the hosts, as the first clients, to also be on the same spec version. Ain't gonna start so soon.

**Jacek Sieka**: About the Fuzzing, how do you drive it? Like how is the Fuzzing driven, what is the input?

**Diederik Loerakker**: The problem with Fuzzing is that we have 2 kinds of inputs:
  1. States
  2. Blocks

The State itself is easily randomized. It contains script traffic contents. It has several validity assumptions.

We are looking to make this extension of the State more intelligent so that you could make more progress in a chain test review of more different pre-states being Fuzzed.

**Jacek Sieka**: What's the difference between that and the YAML file?

**Danny Ryan**: YAML files are particularly constructed tests. Given a pre-state and given some input that we want to hit certain conditions, certain bounds:
  * Maybe a normal path
  * Maybe testing right on the boundary
  * Testing past the boundary

These are particularly constructed tests, something you might write in your own test feed. Whereas these (Fuzzing) are taking pre-states and modifying blocks generally at random, within some sort of bounds, and just applying them to test things that we weren't necessarily thinking about.

**Paul Hauner**: Yeah, I'm not exactly sure how the Ethereum Foundation one works but I know May's explained how our one works
  1. You start with a valid block or some valid object that kind of reaches as far into code path as it can
  2. Then the Fuzzer meters all your code
  3. Then it randomizes the fields of the original object you gave it
  4. Then detects if it explores new code paths

It smartly tries to expand itself out to cover as much code as it can by deterministically, but somewhat randomly, modifying the object and learning about how that affected the coverage.

**Mamy**: The Fuzzing, that proto outline, seemed like it didn't check the bit patterns of the code path that were exercised by the framework.

**Diederik Loerakker**: The randomization of the Block is done by let for sure and that checks the coverage and then tries to randomize as best it could. Just the parts that improve coverage.

And again, you don't want to first only run pre-states, it's more complicated than that.

**Justin Drake**: Yeah it'd definitely coverage driven and there's the randomization aspect.

**Danny Ryan**: Preston has a question:
- "How does the Fuzz harness look: is it libfuzz or is this new tool compatible?"

**Preston**: Diederik Loerakker said that it would be using libfuzz to, basically, you give the signal feedback: did you get farther through the test or was this the worst fuzzing scenario?

**Diederik Loerakker:**: Some people here are already libfuzz's libfuzzer.

What I was just saying about these 2 different kinds of states we're working on. We have the Beacon States and the Block. We don't want to involve only the block inputs because if you're always Fuzzing the same states, you don't get the same coverage as you could if you're Fuzzing multiple states. So this why we're trying to improve on the normal architecture


**Justin Drake**: Did he suggest that the current approach was good enough at exploring many different paths and finding bugs.

Hopefully once we do differential Fuzzing on the Lighthouse, we'll get a bit more confidence.

**Diederik Loerakker:** We get a lot of poor performance because of spec and hopefully also with clients. I think with PySpec is that there are these functions that are not pleasant outs they all inefficiently repeat themselves, not precomputing anything


Now in the next Go spec updates, I optimize, precompute this, precompute that, so we get half, almost client speed spec.


**Danny Ryan**: One of the paths might be to differentially Fuzz against the Go spec and the clients and then if we find issues, to then go back to the Py spec and make sure we agree with what the functionality should be.

We'll keep everyone updated about Fuzzing over the coming weeks.


### 3.2 [Client Updates](https://youtu.be/YB8o_5qjNBc?t=830)

#### 3.2.1 [Nimbus](https://github.com/status-im/nimbus)

**Timestamp: [13:50](https://youtu.be/YB8o_5qjNBc?t=830)**


**Mamy**: We launched our testnet 1, based on libp2p daemon, this morning

We are towards v0.8, all the small changes were integrated and right now a big focus is SSE

We also started to align our State Transition function with PySpec in terms of naming.

We had significant parse improvement during the past week, accumulated 20 to 30x speed-up on the State Transition bench. We identified 3 bottlenecks:
  * In `process_crosslinks(...)` & `get_crosslinke_deltas(...)`. So both combined we had the 10x speed improvement
  * `get_crosslink_committee(...)` via caching, we improved by 2x the speed


If people are interested in seeing what we did, they can reproduce. Since we follow the spec-naming it should be very easy to navigate.
  * [Speed up process_crosslinks(...) and get_crosslink_deltas(...) by 10x - 15x in state_sim #314](https://github.com/status-im/nim-beacon-chain/pull/314)
  * [~2x state_sim speedup via additional caching in get_crosslink_committee #316](https://github.com/status-im/nim-beacon-chain/pull/316)

Published metrics library for Prometheus compact metrics:
  * [Nim metrics client library supporting the Prometheus monitoring toolkit](https://github.com/status-im/nim-metrics)


We have a EWASM research library and we are very happy with. We have started a domain specific language in NIM that compiles to EWASM. It's quite competitive in terms of contract size:
  * [Nimplay is Domain Specific Language for writing smart contracts in Ethereum, using the Nim macro system](https://github.com/status-im/nimplay)

On Ethereum 1, we had some connections issues that were resolved to Parity and Jeff.

#### 3.2.2 [Artemis](https://github.com/PegaSysEng/artemis)

**Timestamp: [17:05](https://youtu.be/YB8o_5qjNBc?t=1025)**

**Jonny Rhea**: We've updated to there especially with the SSE

Also been thinking about a tester slashings, computational requirements for the worst scenario


#### 3.2.3 [Trinity](https://github.com/ethereum/trinity)

**Timestamp: [17:51](https://youtu.be/YB8o_5qjNBc?t=1071)**

**Hsiao-Wei Wang**: Py SSE has been synced to v0.8 and the State Transition update is ongoing. I think it almost there thanks to Alex.

For the networking side, integrating with the Py library, we found some required issues that we need to fix on the upstream library.

We are fixing some interoperability requirements and there is an insecure connections stake.

#### 3.2.4 [Yeeth](https://github.com/yeeth)

**Timestamp: [19:11](https://youtu.be/YB8o_5qjNBc?t=1151)**

**Dean Eigenmann**: I started helping out a bit on Artemis but handed that off again. So now I'm back on updating Yeeth to the latest spec version.

#### 3.2.5 [Harmony](https://docs.ethhub.io/ethereum-roadmap/ethereum-2.0/eth2.0-teams/harmony/)

**Timestamp: [19:37](https://youtu.be/YB8o_5qjNBc?t=1176)**

**Mikhail Kalinin**: Working on an update to v0.8 spec, we're almost there, but SSE part is still in progress.

We started to work on a slot clock mechanism, which is based on network-adjusted time proposed by Vitalik.

We have a PR so far with basic implementation of that protocol. I'm going to take my time on that. Also we have started a small research to investigate into attestation aggregation strategies.
  * [Add draft spec for plaintext key exchange protocol #186](https://github.com/libp2p/specs/pull/186)

The goal is to evaluate an approach that doesn't involve building additional overlays, like handle tree.

Working on minimal libp2p or JVMs.

Worked on multistream implementation recently.


#### 3.2.6 [Lighthouse](https://github.com/sigp/lighthouse)

**Timestamp: [20:57](https://youtu.be/YB8o_5qjNBc?t=1257)**

**Adrian Manning**: Updating lighthouse to v0.8


Have to re-optimize our tree-hash caching to include for more padding nodes.

Defining more extensive HTTP APIs which is working to improve dev experience.


Matt from ConsenSys building out some SSE partials into our codebase.


Slowly been testing an initial version of discovery v5 in small testnets.


Working towards standardizing a minimal libp2p for clients that are using libp2p


In doing so we've had to update our RPC. In particular there's a discussion for the RPC to be using separate protocol IDs per request


[PR where we try to standardize the basic libp2p implementation](https://github.com/ethereum/eth2.0-specs/pull/1281).



#### 3.2.7 [Prysmatic](https://github.com/prysmaticlabs)

**Timestamp: [22:22](https://youtu.be/YB8o_5qjNBc?t=1342)**

**Raul Jordan**: Caught up to v0.8, passing all spec tests.

Issues with Genesis trigger.

There's a lack of coverage for some spec test. Passed all SSE spec tests. Suprised that SSE failed in some Block sanity tests

Having coverage for longer based lists can be good in SSE.

Getting ready for optimizing Prism, code improvements, beautician testing, improvements to clients

#### 3.2.8 [Lodestar](https://github.com/ChainSafe/lodestar)

**Timestamp: [24:03](https://youtu.be/YB8o_5qjNBc?t=1443)**

**Greg Markou**: Trying to upgrade to v0.8.

Began building dev tooling.

Separating out types exclusively so that in Javascript you can import Ethereum 2 types into a React project down in the future. Will help with providers, like a Web3.js provider.

SSE almost up-to-date, ironing out bugs with Proto and Prism.

Should be up-to-date on [SimpleSerialize.com](https://simpleserialize.com/) for open online testing.

We're working towards ensuring that BLS works properly in-browser as well. Peculiar issues there will keep you updated.

Getting Herumi so that we can have some diversity in BLS.

In regards to the client, we comfortable to start doing Block production.

One we finish our update to v0.8, we'll start doing our testnet so that we can see how that plays out.

Then getting that to work in-browser natively.

Getting ready to do dev-tooling.

Also, NIM, we're coming after you guys on the ERC20 contract, we'll get ya.

#### 3.2.9 [Parity](https://github.com/paritytech/parity-ethereum)

**Timestamp: [27:54](https://youtu.be/YB8o_5qjNBc?t=1624)**

**Wei Tang**: Finished the markolization library last week, hopefully, want to extend that into a caching library, but a few missing pieces.

We're trying to update to v0.8 spec, issue we had was in the SSE which was quite a change.

Large refactoring of the codebase.

### 3.3 [Research Updates](https://youtu.be/YB8o_5qjNBc?t=1725)

**Timestamp: [29:08](https://youtu.be/YB8o_5qjNBc)**

#### 3.3.1 [Phase 0](https://docs.ethhub.io/ethereum-roadmap/ethereum-2.0/eth-2.0-phases/)

**Timestamp: [34:50](https://youtu.be/YB8o_5qjNBc?t=2083)**

**Justin Drake**: In parallel to Phase 1 & Phase 2, the research team is doing is more education about Phase 0.

On July 15th 1:00 PM GMT there will be a 2nd Ethereum 2.0 AMA, great opportunity to ask and answer questions related to your implementation work.

Now that the spec is frozen, if you have questions about the design, feel free to reach out. I'm, for example, Justin Drake on Telegram.


#### 3.3.2 [Phase 1](https://docs.ethhub.io/ethereum-roadmap/ethereum-2.0/eth-2.0-phases/)

**Timestamp: [29:08](https://youtu.be/YB8o_5qjNBc)**

**Vitalik Buterin**: On research-side there's a list of To-Do's for Proof-of-Custody and Shard Blocks

Discovered that our approach to light clients that involved Fiat Shimmering and Active Experts didn't particularly make sense.

Simpler approach: Sign over the committee's route and allow clients to verify the committee's route directly. Simplifies and reduces the cost of the client protocol.

But still some decision to make around what the committees are for each slot and how those committees change.

I'd base some of the trade-offs between the properties of light clients and properties of old clients and different kinds of efficiency and safety properties. In general:
  * Phase 0 including in the blocks some of the routes of the persist crosslink committees
  * Phase 1 including a route of the persistent committees

We get a nice, really efficient, light clients. Worst-case: only slightly less efficient, in terms of bytes-per-second, than Bitcoin block headers. Best-case: Much more efficient. There's still just parameters to decide.


Figuring out the exact structure of data in crosslinks; the tradeoff between packing the data tightly versus putting the data for each of the Block headers into a consistent position.

Recently I'm leaning towards packing the data tightly, taking the data for each block-header and block, placing them beside each other. It's one of the possible approaches, not the only.


Not too much to do on the Shard Block side.

Have a PR which, among other things, it switches from multiple attestations and a proposers signature to just having one signature that includes a proposer in the attestations. That there as an option as well.

Not seeing any unexpected difficulties on the Phase 1 side. It's looking better and better.

**Justin Drake**: To add on Phase 1, we're likely to have some cryptanalysis done.  Kovatovich analyze the cryptography that used there.

One of the primitives we're using is the Lujon symbol, as a PRF. It would still be good to have it audited because it's an assumption that's not used in production right now.

#### 3.3.3 [Phase 2](https://docs.ethhub.io/ethereum-roadmap/ethereum-2.0/eth-2.0-phases/)

**Timestamp: [33:06](https://youtu.be/YB8o_5qjNBc?t=1986)**

**Vitalik Buterin**: Not much progress from myself. One of the bigger issues and trade-offs to think about is still how free markets would work. Would be good to get more feedback on that.

The Plasma people are going to release a post on OVM very soon.

**Will Villanueva**: Continuing work on SSE partials.

Will have Phase 1 & Phase 2 testnet, to rally people around having something tangible to test executable environment and other assumptions.

In general, the scout codebase is in Rust.

We'll be going ahead and building that off the work Lighthouse has done to build the prototype. Kicking that off next week.

Started diving into some research connected to Vitalik's post on State Schemes
  * Found a pretty novel approach/idea on how to iterate on that
  * How to build an on-chain multi-shard state scheme that can support generalized contracts
  * This all follows the delayed-state execution model

Posted first-half on Ethereum Research yesterday and we'll be posting the second-half and the applicability to state schemes and Ethereum 2 and multi-shard behavior and what that can open up. Open to feedback on this as there are some cool applications there.
  - [Layer 2 state schemes](https://ethresear.ch/t/layer-2-state-schemes/5691)

The free market stuff we didn't continue diving as we've been in transition, we'll be looking into that these coming weeks.

Team is growing. John Adler is collaborating with us. Trying to grow for Rust-based researchers. Trying to do more research on Phase 1/Phase 2 in parallel to expand a lot of this.

#### 3.3.4 [PegaSys](https://github.com/PegaSysEng)

**Timestamp: [39:28](https://youtu.be/YB8o_5qjNBc?t=2368)**

We continue to work on hold-ups. Nothing yet.

#### 3.3.5 [Runtime Verification](https://github.com/runtimeverification/algorand-verification)

**Timestamp: [39:44](https://youtu.be/YB8o_5qjNBc?t=2384)**

**Musab Alturk**: We have this formalization in the K framework, directly based on the specification.

Migrated to v0.8 and are looking to have something testable.

There's an abstract model, lower priority type of development at the moment, but helpful for the future.

### 3.4 [Network](https://youtu.be/YB8o_5qjNBc?t=2470)


#### 3.4.1 [Libp2p](https://github.com/libp2p/js-libp2p)

**Timestamp: [41:10](https://www.youtube.com/watch?v=YB8o_5qjNBc&feature=youtu.be&t=2470)**

**Mike Goelzer** Grant front, the grant that we're making to Harmony for the minimal JVM libp2p that was mentioned, will be finalized Monday.

We went to chain safe folks who are working most closely on js-libp2p and asked: "hey what would you do to make this production-ready?" They put together a proposal primarily about switching to typesafe Javascript to Typescript and improvements to the documentation and examples.


Are there any concerns on js-libp2p that we should be addressing, either us or chain safe. I want to make a grant to them to get js-libp2p to a production-ready state and I want to include everything.

js-ibp2p has been in production on IPFS, so it's not completely untested. But I do understand that Ethereum might have different requirements.

Any opinions please let me know. Telegram: @MikeGoelzer.

We're working with the Ethereum community to answer questions about what is Protocol Labs relationship to libp2p and about the project in general.When we have written answers to all the question, we will share them with the community.


**Raúl Kripalani**:
* There was a question about insecure transport which is now being used, which Hsio-Wei mentioned we should address at this part of the call.
* We inspect the insecure transport, there was a bug that didn't allow the receiver end of the connection to know about the peer ID that was establishing a connection to them, therefore some things were failing and Go libp2p which made it difficult to produce our interoperability tests. With Go libp2p using insecure transport. So when you want to remove the encryption channel out of the question and just test whether you multiplexing is working, then this is a good approach to do so.
* Between today and tomorrow we'll be adjusting Go libp2p to adhere to the new spec that merged a few days ago. Hopefully, that will unblock any interoperability tests that are pending.

**Jonny Rhea**:
* Hey Mike so you mentioned that libp2p is not-not-production ready?
* Was it broken out of JS IPFS and made into libp2p, what was the flow of that?

**Mike Goelzer**:
* js-libp2p was a part of IPFS and separated into a separate system/github org, but that version (node/javascript) we use now. The history all started in IPFS. js-libp2p and Go libp2p were broken out of the IPFS version. The new Rust libp2p implementation as well. They are all based on the same principles.

**Dean Eigenmann**:
* What is the current state spec? I want my client to connect with other clients.
* Last time I looked at it, Go is also under refactoring.

**Mike Goelzer**:
* We would like libp2p to be a spec-first project. We have a docs writer opening PRs on the specs repo, to define the correct behavior based on what's happening in the Go implementation.
    * [libp2p specification](https://github.com/libp2p/specs)
* In the meantime, we recommend you refer to the Go implementation, which we consider sort of the reference implementation.
* The only major refactor is the core refactor where we pulled out a bunch of interfaces into their repo. That didn't change anything in the wire protocol, it just makes it easier to read.

**Raúl Kripalani**:
* There aren't gonna be further changes to libp2p, only suggestions for bringing different constructs and approaches to do connection management to handle the peer store.
* Those are going to be spec first, you should not any longer expect the implementation to change without there being a spec up-front. We are being very strict about this.
* The place you are where you need to follow a particular implementation should not happen anymore.
* Right now in one record, instead of fifteen, makes it much easier.
* Go through the libp2p specs, there is now an index, table of contents, and open PRs.
* A few weeks ago we lacked a process to define spec maturity, so this is now merged into a meta spectrum. Much more structured.
* A new announcement which unifies a lot of concepts in terms of how connections are handles, how streams are handled, how the connection upgrade process works.
    * [Connections & upgrading #168](https://github.com/libp2p/specs/pull/168/files)

**Dean Eigenmann**:
* I kinda still don't understand on the maturity of the current spec. Going through the Go code, whenever I debug I find some kind of interface, where I end up playing "find the implementation" to figure out what libp2p does.
* So is this spec at a current state where I can implement off that spec, or do I need to keep going through the Go code repeatedly and keep hitting interfaces without clear documentation trying to figure out what those implementations do myself?

**Raúl Kripalani**:
* I understand your frustrations, why don't we do one thing. I'd like to provide a bit of like mentoring right here to understand what the process is when you start from scratch a new implementation on libp2p. It's hard to give a generic answer because the specs are modular, so each spec will have a different maturity.
* Maybe we get in a call offline and establish a channel of communication and guide you through the process.

**Raúl Kripalani**:
* About the unsecured transport, does that means it's an unencrypted clear-text channel?

**Raúl Kripalani**:
* Yes, not for use in production. Intended only for testing. It didn't work against other implementations in libp2p. It only worked internally. Now that we have a hybrid ecosystem, there are others that are trying to test their inner pieces that come after the security handshake that does not rely on a secure channel, like multiplexing or other protocols. There is some value in having a standardized and secure transport, ONLY FOR TESTING PURPOSES.

**Jacek Sieka**
* Assuming that some client doesn't have SECIO implemented yet, then they can start using this more simple one.

**Raúl Kripalani**:
* Yes, allows MPLEX person to test against an insecure version, while other work on SECIO.

**Jacek Sieka**
* Does it authenticate?

**Raúl Kripalani**:
* The initial handshake, the initiating peer should have a peer ID, the receiving end is exchanging its peer ID and its public key, so it can check it is them. But subsequent messages/bytes are not authenticated.

**Whiteblock**:
* Question about libp2p, back to Mike's point about production readiness of the rest of libp2p.
* I believe Gossip Sub has been implemented by chain safe and is not used by IPSF?

**Mike Goelzer**:
* Yeah, that is correct.

**Whiteblock**:
* That would be something to ensure it is production ready.

**Mike Goelzer**:
* Fair point, there are some features that Ethereum 2 cares about that are part of the system, IPFS isn't battle testing them.

**Raúl Kripalani**:
* For the record, I think the IPFS team would be super happy to intake Gossip Sub and to add an experimental flag to enable it, just like the Go IPFS project has done and even conduct interoperability testing out in the wild, with IPFS and Gossip Sub enabled on both Go and JS.

**Greg Markou**:
* Yeah, for transparency, the main reason I want to have more than just looking at it.
* As we approach doing light client, I wanna make sure that people can have a chrome extension light client in their browser that's gonna have to rely exclusively on Gossip Sub, so I want to take steps to make that harden.

**Raúl Kripalani**:
* I will start a conversation to integrate your work, Gossip Sub, into IPFS as a medium for shipping it to an actual finished product to the world.
* Secondly, we are working on a testlab infrastructure that would allow us to deploy different clients at scale and test interactions between them and so-on.
* Then we can look at other projects using js-libp2p, including MetaMast, to implement Gossip Sub and test it.

**Benjamin Burns**:
* Is there a date you plan to have the specs finalized, to the point where you expect people to implement against them rather than the Go code?

**Mike Goelzer**:
* Not a date yet, but this question came up. We will update you next time on the decision there.
* The biggest bottleneck for us is we need to hire a second specs writer
    * If anyone can refer someone who is looking for a job and does technical writing?

**Whiteblock**:
* Does it need to be hired? How can we help you as a community to get it done?

**Mike Goelzer**:
* We definitely would be receptive to PRs, people who understand the Go codebase well would be the best one to write specs for it.
    * The person to contact is Yusef Napora, who is responsible for writing the specs right now. Ping him on Github and ask him where's a place to focus on.
    * [Yusef Napora's Github](https://github.com/libp2p/specs/commits?author=yusefnapora)

**Raúl Kripalani**:
* Create a pipeline in a public calendar and create a status-matrix where people can see what the state is of each element is and get involved. We should create an issue for each of them, so people who want to help can jump in and help.

**Whiteblock**:
* Do you want to open some Gitcoin grants or bounties to speed up the things?

**Mike Goelzer**:
* We are open to making grants.
* We haven't been using Gitcoin, would like to, but haven't had time to.
* If there are people who are interested in grant-work for improving the specs, they should get in touch with us.

**Danny Ryan**:
* I do want to highlight this PR that was the combining of two other PRs
* There's some already some good conversation on here, but I do want someone from each team to look at this and participate. Something we want to get merged soon and iterate on. So please take a look at PR #1281
    * [Libp2p Standardization Update #1281](https://github.com/ethereum/eth2.0-specs/pull/1281)
* Adrian, anything you want to say on that before we move on?

**Adrian Manning**:
* Not really, ideally if people can look and give opinions, we can modify it.

**Jacek Sieka**:
* Do you anticipate that we can use the same discovery for Eth1 and Eth2 at some point?

**Adrian Manning**:
* We're using DISC v5 at the moment.

**Danny Ryan**:
* If the question is "if Eth1 is getting migrated to v5", the answer is yes.
* The intention is to use the same unified discovery in parallel across both protocols.
* Discussion with some people that are doing an audit on the protocol DISC v5. Expects iterative on the spec after it finishes, then performance.


#### 3.4.2 Gossiping Mechanism and [Episub](https://github.com/libp2p/specs/blob/master/pubsub/gossipsub/episub.md)—Artemis, Prysmatic Labs, Lodestar Handles Exchange

**Timestamp: [1:07:56](https://youtu.be/YB8o_5qjNBc?t=4076)**

**Whiteblock**:
* Internal last week we had three common teams in the same room: Artemis, Prysmatic Labs, Lodestar.
* Able to have an exchange of handles between Prysmatic and Artemis using the Simple Hobbits approach.
* We are learning on that, most of the ugly bits have been on the people collaborating and not the technical side. Given the Hobbits is not too complex.
* Next level, the ability to Gossip bits between the different instances.
    * We're also trying to gauge from the Moloch DAO tester and all the valuable work that we did into creating this type of testnet, what would it take to create a test-bench where we would be able to really create a Genesis even, make it possible for all the peers to recognize each other even over a static hearing is fine for now. And to start having an exchange of block attestations, making sure that it's working all the time.
* There are separate efforts in parallel:
    * One is to work on the gossipping approach. Right now the gossip is extremely simple. We simply tell everyone we have a block and they can ask for it, or we have an attestation and they can ask for it.
    * The other side, we're working on all sorts of utilities and tools so it's possible for the community to run a testnet with the various clients, so there are several stylization items around the keystore. On making sure we can all generate the same genesis event and it can work with a gift note on the local network, it can generate that from its state of a contract being deployed there.
* At white block we can snapshot the state and so we create testnet where the state is already snapshotted. We will be using that tech as much as possible to shorten the dev cycles. It takes quite a bit to create the whole set-up every time.

**Danny Ryan**:
* Some client are currently gossiping hashes and doing RPC calls for retrieval of that data.
* We assume that the latency of that will be too high and gossiping full objects is going to be the proper path.

**Whiteblock**:
* Right, we cripple this to a point where it's very very simple for the reason of just having interoperability.
* At collection time you want to use something like Gossip Sub or even Episub where we can really tune-in the number of peers and have propagation that is impossible to stop, from a network perspective, the propagation of a message. But it's also much easier on the network.
* All this needs to be benchmarked, so that helps us increment to increase advancements.

**Jonny Rhea**:
* At Preston's suggestion, that we simplify the gossiping mechanism.
* The egress or ingress charges were high on GCP, and that methodology help cut the cost down. Is that right Preston?

**Preston**:
* I think what you're referring to is when we're creating the announcement messages?
* So if we've created a new block, will announce the hash of it, which is of constant size.
* That gets gossiped to the entire network and if people hear it redundantly, they're not getting this redundant large data, they're only getting a small piece.
* I tell you this new block and if you want it, you dial back and ask me what the data is.
* That's been helping us same some data there.
* In terms of keeping it simple, I think that for the Hobbit's implementation. Don't undertake this and get it super complex because it's just to see basic interops, so I was advocating keeping that simple as well.

**Danny Ryan**:
* What I'm saying though is that announcement of identifier and subsequent request, though does same bandwidth, I think is gonna induce way to high of latencies on the network.
    * Because at the beginning, nobody knows about it. So you're strictly wasting time.
* Potentially there's a hybrid strategy where maybe a portion to the slot you're gossiping identifier, but I don't the extreme of strictly gossiping identifier at the beginning is gonna be the proper way.

**Preston**:
* I would agree with that for blocks because those have some big urgency, but for attestations, it's not as urgent and you can still get away with broadcasting a subset of it without having to do the full data.
* It's worth looking into, but I agree there's now a round trip if you're trying to get blocks out pretty quickly.

**Jonny Rhea**:
* Danny, your suggestion is very similar to Episub or Epidemic Broadcast Trees, just FYI that hybrid approach.


**Danny Ryan**:
* Jannik, we did do some experimentation on Episub awhile ago. What were your findings there?

**Jannik Luhn**:
* That it didn't have much, if at all.
* Episub is different from what Danny just suggested because it's not based on timing.
* If I understood correctly, he wanted to basically send four blocks in the first half of the slot and then only hashes in the second half? Whereas in Episub you just keep track of what information you receive from which peer and then you decide on what to send to that peer again?

**Jonny Rhea**:
* It's still a hybrid approach because you have the actual gossiping of the full block if it's an eager peer and if it's a lazy peer you just tell it "hey I have this". It splits the difference is my point.

**Kevin Main-Hsuan Chia**:
* I think it's already in the Gossip Sub, that I want and I have this thing.

**Whiteblock**:
* Really? Because I think Gossip Sub is probabilistic.

**Jonny Rhea**:
* Yeah, that was my understanding too.

**Whiteblock**:
* I don't know that any subs that we implemented, since we have libp2p guys on the call, what's the level of maturity of Episub?

**Raúl Kripalani**:
* Episub was an idea in the pipeline, but not highly prioritized right now.
* Where Episub is optimal, is when you have very stable dissemination patterns in the network. So very few producers and a lot of consumers in the network.
* Therefore Episub, by using the tree and broadcast screens, you're able to figure out the best-spanning tree in the network to disseminate messages. That is coming from a very small set of producers.
* We don't have that pattern, that's why we haven't prioritized that. But if this is the case for Eth 2.0, then definitely worth reactivating this discussion.

**Jonny Rhea**:
* I'd be interested if someone has looked into what's best for gossiping blocks as opposed to attestations if we've thought about that.
* That's a good point, Raúl, by the way. As far as the trade-offs.

**Kevin Main-Hsuan Chia**:
* I just want to add that I think the message identifier scheme is sorting process up now.
* Episub is more like you grab and prune the agents, their peer connections. It's a different scenario.
* I think Jannik has done some pull-push simulation before?

**Jannik Luhn**:
* That was similar to Danny and such tested, but I don't remember why.

**Raúl Kripalani**
* Is there a reason you believe an Epidemic Broadcaster approach could be efficient for pool in this message propagation paradigm that you have in Eth 2.0?

**Jonny Rhea**:
* I don't know, just let me know, speculate and throw something out there.
* Maybe gossip sub is better for gossiping blocks and attestation is better for attestations.
* Reverse that, Episub is better for blocks and Gossip sub is better for attestations.

**Danny Ryan**:
* I guess I'm not certain, I know that the Beacon chain subnet would probably be more stable over time, whereas these other topics may alter quickly.
* There might be a trade-off between what gossiping we're using for short subnets versus beacon subnet. I'm not certain.

**Raúl Kripalani**:
* As a way forward to continue discussing this topic, if somebody could put together maybe a small blurb on what the difference is in message propagation on these particular circuits, then I can involve someone on the libp2p team who is a gossiping specialist. Asking them if we could have a hybrid router that we could attach specific dissemination routing strategies for one topic, and a different routing for a different topic, and so on, and somehow arrive at different pots in the network.

**Danny Ryan**:
* I have some notes on this that describe the timing of the broadcast as well as the size and can add some notes about the stability of topics and stuff. I will pass it on to you.

**Jacek Sieka**:
* I want to point out that all these schemes introduce extra opportunities for failures and issues in general.
* The absolute minimum approach of gossiping full blocks is very very resilient. It's full-proof so-to-speak.
* Anything on top of that, we should be very careful of motivating that with substantial gains, because the simplicity of normal flooding makes it extremely resilient against all kinds of attacks.

**Whiteblock**:
* One way to address this
    * Whatever gossiping protocol we end up choosing we have this baseline where it's always possible to going back to flooding and it works.
* An adaptable approach where we start with flooding. We can maybe optimize it down the road, but we need to test that.
* Did some testing of Flood Sub with Wedlock, it does not perform in the period with the number of bytes which are required for blocks, by the Eth 2.0 protocol.
* But I might be wrong, I think there's more research and testing needed there. That's what we know at this point.

**Jacek Sieka**:
* Gossip sub was chosen for its substantial improvements in early experiments.

**Raúl Kripalani**
* Let me provide some insight there to how you make decisions regarding which gossiping pattern to choose. Generally, it's all a matter of trade-offs.
    * Flood Sub is very resilient to all kinds of attacks as it's very naive. The key's simplicity here, so you just broadcast messages to every single peer that you connected to that you believe is interested in that message.
        * However, that introduces a massive amplification factor on IO, which depending on the traffic, the volume, the size of the messages, the latency of links, and several things, could potentially harm more than benefit. So that's one trade-off.
    * Then as you start cutting down on the amplification factor because you say well if these peers are supposed to be redundantly connected and indirectly redundantly connected. So a particular message may arrive at a peer way too many time due to the amplification factor, then you do wanna start getting more intelligent to how you tell peer "stop sending me this redundant message".
        * Your trade-off here could be to reduce write amplification and overall traffic in the network.
* Happy to continue the discussion. Tests are measuring Gossip Sub that needs to be revisited, that tested the wrong things.
* Open to exploring different approaches. Understanding training down to the requirements to understand if a hybrid between Gossip Sub and Epi Sub, or Flood Sub as a fallback, could even advance the state of the art in the way these algorithms could be implemented.


### 3.5 [Spec Discussion](https://youtu.be/YB8o_5qjNBc?t=5095)

**Timestamp: [1:24:57](https://youtu.be/YB8o_5qjNBc?t=5095)**

**Danny Ryan**:
* I know implementers mentioned the SSE. There were a couple more escape types that were added to SSE, specifically the Bit List and Bit Vector, that moves some of the low-level validation of bytes out the spec and into the typing system.
* This was done:
    1. To make the spec focus more on spec things and not low-level byte manipulation and byte validation.
    2. Was also done to provide a valuable set of types in SSE that might be used in other places, such as the application area.
* If there is byte-level stuff you need to be doing, why repeat the logic in multiple places when we can add it to the type system.
* there are some issues, so I want to open it up for a quick decision so that we can fix it if we need to.
* Dankrad, I know you did a lot of work on it and facilitating a lot of conversation around it. Do you have anything to add?

**Dankrad Feist**:
* We want to understand pain-points here.
* I think it's valuable to have in the SSE stack, but we don't want to make life super hard for the implementers.

**Danny Ryan**:
* This is not something I want to leave hanging. If you want to discuss this, feel free to open the issue and we'll discuss there over the next seven days. Otherwise, this is very critical for getting aligned with ConsenSys tests.

**Mamy Ratsimbazafy**:
* Just as a comment, the more types we have defined in the SSE spec the more efficient our code, at least in NIM, can be. In terms of both code size and performance, because we have much less to check and we can insert the proper deserializing code in our codebase.

**Danny Ryan**:
* Gotcha, thanks.
* We have a few minutes left. Are there any questions left?

**Diederik Loerakker**:
* About SSE, there's this minor thing, where we can have, fixed-size, empty containers, and empty vectors. It's kinda troublesome.
* I know we don't currently have them in the spec. I just wanted to address it so the SSE spec could be complete.
* What do clients like best?
    * Do we want to make empty vector illegal?
    * Or do we want to make lists containing them illegal?
* Is there a use case for empty, fixed-size, containers?

**Vitalik Buterin**:
* Well, we already made them illegal. So we're revisiting that decision.

**Diederik Loerakker**:
* We made vectors illegal, but we also have containers. Then there's this inconsistency between lists being zero and vectors not being zero.
* So I just want to get this right and then we can move on.

**Dankrad Feist**
* So before containers and empty vectors, they're both illegal, and now we added this new thing that lists suddenly have a limited size.
* Suddenly we have the question, "can that size be zero?"
    * It doesn't cause the same problems as it does for vectors or containers, because it would still be a variable size type, so all the information would be needed.
* The question's just, "is it kinda weird that we forbid one thing and not the other?"

**Vitalik Buterin**:
* I'm okay forbidding, or not forbidding, lists with zero max length.

**Dankrad Feist**
* The only question why you want to forbid it is because it might give us an easy way to "comment out some features" in the spec by setting the max length to zero.

**Diederik Loerakker**:
* We already discussed this issue. If any implemented would need this kind of type, please join the issue in the specs repository. Otherwise, I think it's not too important.


### 3.6 [Open Discussion/Closing Remarks](https://youtu.be/YB8o_5qjNBc?t=5540)

**Timestamp: [1:32:20](https://youtu.be/YB8o_5qjNBc)**

**Danny Ryan**: Any other things before we close today?

**Joseph Delong**: For the interop, I just wanna say that the invitations went out to team leads. Those invitations are good until the 14th. And for the Antoine's in the call, that's Bastille Day.

After that, we're gonna reshuffle and send out more invitations to some of the teams that are wanting to attend. So make sure that you register.

There are a bunch of teams that haven't registered. Please do register in the next 3 days.

**Danny Ryan**: It's easy and free to register.

We'll meet in 2 weeks, take a look at the calendar first. See ya.
