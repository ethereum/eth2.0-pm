# Ethereum 2.0 Implementers Call 21 Notes

## Contents

- [Contents](#contents)
- [1 Meeting Details](#1-meeting-details)
- [2 Attendees](#2-attendees)
- [3 Agenda](#3-agenda)
	- [3.1 Testing Updates](#31-testing-updates)
		- [3.1.1 Overflow in Slashing](#311-overflow-in-slashing)
		- [3.1.2 Spec Freeze](#312-spec-freeze)
		- [3.1.3 Fuzzing](#313-fuzzing)
	- [3.2 Client Updates](#32-client-updates)
		- [3.2.1 Nimbus](#321-nimbus)
		- [3.2.2 Artemis](#322-artemis)
		- [3.2.3 Trinity](#323-trinity)
		- [3.2.4 Yeeth](#324-yeeth)
		- [3.2.5 Harmony](#325-harmony)
		- [3.2.6 Lighthouse](#326-lighthouse)
		- [3.2.7 Prysmatic](#327-prysmatic)
		- [3.2.8 Lodestar](#328-lodestar)
		- [3.2.9 Parity](#329-parity)
	- [3.3 Research Updates](#33-research-updates)
		- [3.3.1 Phase 0](#331-phase-0)
		- [3.3.2 Phase 1](#332-phase-1)
		- [3.3.3 Phase 2](#333-phase-2)
		- [3.3.4 PegaSys](#334-pegasys)
		- [3.3.5 Runtime Verification](#335-runtime-verification)
	- [3.4 Network](#34-network)
		- [3.4.1 Libp2p](#341-libp2p)
		- [3.4.2 Gossiping Mechanism](#342-gossiping-mechanism)
	- [3.5 Spec Discussion](#35-spec-discussion)
	- [3.6 Open Discussion/Closing Remarks](#36-open-discussionclosing-remarks)



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

**Danny Ryan**: Prysmatic Labs, Terence [Tsao], found an issue where the calculation and slashing was potentially overflowing. Relatively non-substantive changes (fixes, documentation, etc.) in v08x branch [#1286](https://github.com/ethereum/eth2.0-specs/pull/1286) includes a fix to this.  This will branch will get out in the next few days.

#### 3.1.2 [Spec Freeze](https://github.com/ethereum/eth2.0-specs/pull/1242)

**Timestamp: [5:12](https://youtu.be/YB8o_5qjNBc?t=309)**

**Diederik Loerakker**: Spec Freeze is over now, can stop throwing up to the spec and build.

#### 3.1.3 [Fuzzing](https://github.com/ethereum/eth2.0-specs/tree/dev/test_libs/pyspec/eth2spec/fuzzing)

**Timestamp: [6:51](https://youtu.be/YB8o_5qjNBc?t=411)**


**Justin Drake**: The goal is to provide basic fuzzing infrastructure for all the clients. The purpose is so Client implementers don't have to worry too much about being compliant with the State Transition Function.

We've started with pyspec and the goal executable specs. The next target for integration may be Lighthouse. A lot of the infrastructure will be generic for clients. May come in the next two weeks.

**Diederik Loerakker**: We are fuzzing v0.8.0, Go executable spec is almost up-to-date now, pyspec already is up-to-date.

**Jacek Sieka**: What is the input for fuzzing?

**Diederik Loerakker**: The problem with Fuzzing is that we have 2 kinds of inputs:
  1. State
  2. Blocks

We are mostly focusing on Blocks now. We are looking to make this extension of the State more intelligent, to make something like a chain-test with more differing presets.

**Jacek Sieka**: What's the difference between that and the YAML file?

**Danny Ryan**: YAML files are particularly constructed tests, something you might write in your own test feed. Given a pre-state and given some input that we want to hit certain conditions, certain bounds:
  * Maybe a normal path
  * Maybe testing right on the boundary
  * Testing past the boundary

Whereas these (Fuzzing) are taking pre-states and modifying blocks at random, within some sort of bounds, to test things that we weren't necessarily thinking about.

**Paul Hauner**: How ours works (not Ethereum Foundations version):
  1. Start with a valid block or valid object that reaches far into the code path
  2. The Fuzzer meters all your code
  3. Randomizes the fields of the starting object
  4. Detects if it explores new code paths

It expands broadly, partially randomly modifies the object, and learns how that affected coverage.

**Mamy**: That fuzzing outline seemed like it didn't check the bit patterns of the code path that were exercised by the framework.

**Diederik Loerakker**: The randomization of the Block is done by let and that checks the coverage and then tries to randomize as best it could, but only the parts that improve coverage.

Again, you don't want to first only run pre-states, it's more complicated than that.

**Justin Drake**: It's definitely coverage driven and with a randomization aspect.

**Danny Ryan**: Preston has a question:
>"How does the Fuzz harness look: is it libfuzz or is this new tool compatible?"

**Preston**: Diederik Loerakker said that it would be using libfuzz to give the signal feedback: "Did you get farther through the test or was this the worst fuzzing scenario?"

**Diederik Loerakker:**: Some people here are already familiar with libfuzzer.

With these two states, Beacon States and the Block, we don't want to involve only the block inputs. If you always Fuzz the same states, you don't get the same coverage as Fuzzing multiple states. We're trying to improve on the normal architecture.

It is similar to libfuzzer, yes.

**Justin Drake**: The current approach was good enough at exploring many different paths and finding bugs. The main limit is the speed of pyspec.

Hopefully once we do differential Fuzzing on the Lighthouse and go-spec, we'll get a bit more confidence.

**Diederik Loerakker:** I think with pyspec there are these functions which all inefficiently repeat themselves, not precomputing anything.

In the next go-spec updates, I optimize, precompute this, precompute that, so we get half, almost client speed, spec.

**Danny Ryan**: One path might be to differentially Fuzz against the go-spec and the clients, and then if we find issues, to then go back to the Py spec and make sure we agree with what the functionality should be.

We'll keep everyone updated about Fuzzing over the coming weeks.


### 3.2 [Client Updates](https://youtu.be/YB8o_5qjNBc?t=830)

#### 3.2.1 [Nimbus](https://github.com/status-im/nimbus)

**Timestamp: [13:50](https://youtu.be/YB8o_5qjNBc?t=830)**


**Mamy**: We launched our testnet 1, based on libp2p daemon, this morning.

We are working towards v0.8. All the small changes were integrated and right now a big focus is SSE.

We also started to align our State Transition function with pyspec in terms of naming.

We had significant parse improvement during the past week, accumulated 20 to 30x speed-up on the State Transition bench. Links, if people are interested in seeing what we did, so they can reproduce:
  * [Speed up process_crosslinks(...) and get_crosslink_deltas(...) by 10x - 15x in state_sim #314](https://github.com/status-im/nim-beacon-chain/pull/314)
  * [~2x state_sim speedup via additional caching in get_crosslink_committee #316](https://github.com/status-im/nim-beacon-chain/pull/316)

Published metrics library for Prometheus compact metrics:
  * [Nim metrics client library supporting the Prometheus monitoring toolkit](https://github.com/status-im/nim-metrics)


We have a EWASM research library we are very happy with. We have started a domain specific language in NIM that compiles to EWASM. It's quite competitive in terms of contract size:
  * [Nimplay is Domain Specific Language for writing smart contracts in Ethereum, using the Nim macro system](https://github.com/status-im/nimplay)

On Ethereum 1, we had some connections issues that were resolved to Parity and Geth.

#### 3.2.2 [Artemis](https://github.com/PegaSysEng/artemis)

**Timestamp: [17:05](https://youtu.be/YB8o_5qjNBc?t=1025)**

**Jonny Rhea**: We've updated, especially with the SSE.

Also been thinking about a tester slashings, computational requirements for the worst scenario.

We see the need to investigate the network load, decide what strategy to use when activating.


#### 3.2.3 [Trinity](https://github.com/ethereum/trinity)

**Timestamp: [17:51](https://youtu.be/YB8o_5qjNBc?t=1071)**

**Hsiao-Wei Wang**: Py SSE has been synced to v0.8 and the State Transition update is ongoing. Its almost there thanks to Alex.

For the networking side, integrating with the Py library, we found some required issues that we need to fix on the upstream library.

We are fixing some interoperability requirements.

There is an insecure connections stake, which will be brought up in the Networking section of the call.

#### 3.2.4 [Yeeth](https://github.com/yeeth)

**Timestamp: [19:11](https://youtu.be/YB8o_5qjNBc?t=1151)**

**Dean Eigenmann**: Was working with Artemis, but back to updating Yeeth to the latest spec version.

#### 3.2.5 [Harmony](https://docs.ethhub.io/ethereum-roadmap/ethereum-2.0/eth2.0-teams/harmony/)

**Timestamp: [19:37](https://youtu.be/YB8o_5qjNBc?t=1176)**

**Mikhail Kalinin**: Working on an update to v0.8 spec, we're almost there, but SSE part is still in progress.

We started to work on a slot clock mechanism. We have a PR so far with basic implementation of that proposal.

We have started a small research to investigate into attestation aggregation strategies. The goal is to evaluate an approach that doesn't involve building additional overlays.
  * [Add draft spec for plaintext key exchange protocol #186](https://github.com/libp2p/specs/pull/186)

Working on minimal libp2p or JVMs.

Worked on multistream implementation recently.


#### 3.2.6 [Lighthouse](https://github.com/sigp/lighthouse)

**Timestamp: [20:57](https://youtu.be/YB8o_5qjNBc?t=1257)**

**Adrian Manning**: Updating lighthouse to v0.8. We have to re-optimize our tree-hash caching to include for more padding nodes.

Defining more extensive HTTP APIs which is working to improve dev experience.

Matt from ConsenSys is building out some SSE partials into our codebase.

Slowly been testing an initial version of discovery v5 in small testnets.

Working towards standardizing a minimal/final libp2p for clients using libp2p.

The libp2p work lead to updating our RPC. There's been discussion for the RPC to use separate protocol IDs per request:
- [PR where we try to standardize the basic libp2p implementation](https://github.com/ethereum/eth2.0-specs/pull/1281).



#### 3.2.7 [Prysmatic](https://github.com/prysmaticlabs)

**Timestamp: [22:22](https://youtu.be/YB8o_5qjNBc?t=1342)**

**Raul Jordan**: Caught up to v0.8, passing all spec tests.

Issues with Genesis trigger.

There's a lack of coverage for cases of spec test. Passed all SSE spec tests. Surprised that SSE failed in some Block sanity tests.

Getting ready for optimizing Prism, working on code improvements, beautician testing, and generally more robust improvements to the client.

#### 3.2.8 [Lodestar](https://github.com/ChainSafe/lodestar)

**Timestamp: [24:03](https://youtu.be/YB8o_5qjNBc?t=1443)**

**Greg Markou**: Trying to upgrade to v0.8.

Began building dev tooling. Will help with providers, like a Web3.js.

SSE almost up-to-date, ironing out bugs with Proto and Prism.

Should be up-to-date on [SimpleSerialize.com](https://simpleserialize.com/) for open online testing.

We're working towards ensuring that BLS works properly in-browser as well. Some peculiar issues there, will keep you updated.

Working to using Herumi so that we can have some diversity in BLS.

In regards to the client, comfortable to start doing Block production. Once we finish our update to v0.8, we'll start doing our testnet. Then getting it to work in-browser.

Going back onto assembly script.

Also, NIM, we're coming after you guys on the ERC20 contract, we'll get ya.

#### 3.2.9 [Parity](https://github.com/paritytech/parity-ethereum)

**Timestamp: [27:54](https://youtu.be/YB8o_5qjNBc?t=1624)**

**Wei Tang**: Finished the markolization library last week, hopefully, want to extend that into a caching library, but there are still a few missing pieces.

We're trying to update to v0.8 spec. The issue we had was in the SSE, a substantial change for us. Large refactoring of the codebase.

### 3.3 [Research Updates](https://youtu.be/YB8o_5qjNBc?t=1725)

**Timestamp: [29:08](https://youtu.be/YB8o_5qjNBc)**

#### 3.3.1 [Phase 0](https://docs.ethhub.io/ethereum-roadmap/ethereum-2.0/eth-2.0-phases/)

**Timestamp: [34:50](https://youtu.be/YB8o_5qjNBc?t=2083)**

**Justin Drake**: In parallel to Phase 1 & Phase 2, the research team is doing is more education about Phase 0. Educational documents have been made.

On July 15th 1:00 PM GMT there will be a 2nd Ethereum 2.0 AMA, an opportunity to ask questions related to your implementation work.

Now that the spec is frozen, feel free to reach out with questions about the design. I'm Justin Drake on Telegram.


#### 3.3.2 [Phase 1](https://docs.ethhub.io/ethereum-roadmap/ethereum-2.0/eth-2.0-phases/)

**Timestamp: [29:08](https://youtu.be/YB8o_5qjNBc)**

**Vitalik Buterin**: On research-side there's a list of To-Do's for Proof-of-Custody and Shard Blocks.

Discovered our approach to light clients, involving Fiat Shimmering and Active Experts, didn't make sense.

Found a simpler approach: Sign over the committee's route and allow clients to verify the committee's route directly. There's still some decisions to what committees are for each slot and how those committees change.

In general:
  * Phase 0, including in the blocks a route of the crosslink committees should be fine
  * Phase 1, including a route of the persistent committees

We get nice, really efficient, light clients. There's still just parameters to decide.

Figuring out the exact structure of data in crosslinks.

Not too much to do on the Shard Block side.

Have a PR which switches from multiple attestations and a proposers signature to just having one signature that includes a proposer in the attestations. That's an option as well.

Not seeing any unexpected difficulties on the Phase 1 side. It's looking better and better.

**Justin Drake**: To add on Phase 1, we're likely to have some cryptanalysis done.  We might have Kovatovich analyze the cryptography used there.

One of the primitives we're using is the Lujon symbol, as a PRF. It would still be good to have it audited because it's an assumption not used in production right now.

#### 3.3.3 [Phase 2](https://docs.ethhub.io/ethereum-roadmap/ethereum-2.0/eth-2.0-phases/)

**Timestamp: [33:06](https://youtu.be/YB8o_5qjNBc?t=1986)**

**Vitalik Buterin**: Not much progress from myself. One of the bigger issues and trade-offs to think about is still how free markets would work. Would be good to get more feedback on that.

The Plasma people are going to release a post on OVM very soon.

**Will Villanueva**: Continuing work on SSE partials.

Will have prototype Phase 1 implementation. Will have Phase 1 & Phase 2 testnets. In general, the scout codebase is in Rust. The prototype will extend the work from Lighthouse. Kicking that off next week.

Started diving into some research connected to Vitalik's post on State Schemes:
  * Found a pretty novel approach/idea on how to iterate on that
  * How to build an on-chain multi-shard state scheme that can support generalized contracts
  * This all follows the delayed-state execution model

Posted first-half on Ethereum Research yesterday and we'll be posting the second-half and the applicability to state schemes and Ethereum 2 and multi-shard behavior and what that can open up. Open to hearing feedback on this.
  - [Layer 2 state schemes](https://ethresear.ch/t/layer-2-state-schemes/5691)

Free markets, we didn't continue diving as we've been in transition. We'll be looking into that these coming weeks.

Team is growing. John Adler is collaborating with us. Trying to grow for Rust-based researchers as well. Trying to do more research on Phase 1/Phase 2, more Phase 2 focus, in parallel to expand a lot of this.

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

**Mike Goelzer** The grant to Harmony for the minimal `jvm-libp2p` will be finalized Monday.

For making `libp2p` production ready, Chain Safe put together a proposal, primarily about switching to typesafe Javascript (to Typescript) and improvements to the documentation and examples.

Are there any concerns on `js-libp2p` that we should be addressing, either us or Chain Safe? I want to make a grant to them to get `js-libp2p` to a production-ready state and I want to include everything.

Any opinions please let me know. Telegram: @MikeGoelzer.

We're working with the Ethereum community to answer questions about what Protocol Labs relationship is to `libp2p` and the project in general. When we have written answers to all the questions, we will make it public to share.

**Raúl Kripalani**: There was a question about insecure transport.

There was a bug that didn't allow the receiver end of the connection to know about the peer ID that was establishing a connection.

Between today and tomorrow we'll be adjusting `go-libp2p` to adhere to the new spec that merged a few days ago.

**Jonny Rhea**: Was `libp2p` broken out of `js-ipfs` and made into `libp2p`, and what was the flow of that?

**Mike Goelzer**: Initially, `js-libp2p` was a part of IPFS and made a separate system, but now it's what `js-ipfs` uses today.

All `libp2p` implementations are based on the same principles `go-libp2p` and `js-libp2p` use.

**Dean Eigenmann**: What is the current state spec?

**Mike Goelzer**: We would like `libp2p` to be a spec-first project. We have a docs writer opening PRs on the specs repo, to define the correct behavior based on what's happening in the Go implementation.
    * [libp2p specification](https://github.com/libp2p/specs)

In the meantime, we recommend you refer to the Go implementation.

**Raúl Kripalani**: There aren't gonna be further changes to `libp2p`. But, we're taking suggestions.

You should not any longer expect the implementation to change without there being a spec up-front. We are being very strict about this.

Updates made to `libp2p` specs to make it more organized (table of contents, index, etc.).

We merged the specs lifecycle and maturity meta-spec.

This spec serves as a unifying spec, that ties a lot of concepts seen in other specs:
 - [Connections & upgrading #168](https://github.com/libp2p/specs/pull/168/files)

**Dean Eigenmann**: Is this spec at a state where I can implement off that spec, or do I need to go through the Go code, hitting interfaces without clear documentation?

**Raúl Kripalani**:
It's hard to give a generic answer because the specs are modular. Each spec will its own maturity.

Maybe we get in a call offline to guide you through the process.

**Raúl Kripalani**: Unsecured transport, does that means it's an unencrypted clear-text channel?

**Raúl Kripalani**: Yes, not for use in production. Intended only for testing.

**Jacek Sieka** Assuming that some client doesn't have SECIO implemented yet, then they can start using this more simple one?

**Raúl Kripalani**: Exactly.

**Jacek Sieka** Does it authenticate?

**Raúl Kripalani**: The initial handshake authenticates. But subsequent messages/bytes are not authenticated.

**Whiteblock**: On `js-libp2p`, I believe Gossip Sub has been implemented by Chain Safe and is not used by IPSF?

**Mike Goelzer**: Yes, not integrated in IPFS.

**Whiteblock**: That would be something to ensure it is production ready.

**Mike Goelzer**: Fair point, there are some features that Ethereum 2 cares about that IPFS isn't battle testing. We need to do testings on Gossip Sub.

**Raúl Kripalani**: I think the IPFS team would be happy to intake Gossip Sub and to add an experimental flag to enable it.

**Greg Markou**: As we approach doing light client, that's a main focus. Chrome extension light clients will need to rely exclusively on Gossip Sub. What steps will you take to make that harden?

**Raúl Kripalani**: I will start a conversation to integrate your work, Gossip Sub, into IPFS.

Secondly, we are working on a testlab infrastructure that would allow us to deploy different clients at scale and test interactions between them and so-on.

We can look at other projects using `js-libp2p`, including MetaMast, to implement Gossip Sub and test it.

**Benjamin Burns**: Is there a date you plan to have the specs finalized?

**Mike Goelzer**: Not a date yet, we were talking about creating one. We will update you.

The biggest bottleneck for us is we need to hire a second specs writer. Looking for referrals for a documentation writer.

**Whiteblock**: Does it need to be hired? How can we help you as a community to get it done?

**Mike Goelzer**: We would be receptive to PRs. People who understand the Go codebase well would be best.

The person to contact is Yusef Napora, who is responsible for writing the specs right now.
- [Yusef Napora's Github](https://github.com/libp2p/specs/commits?author=yusefnapora)

**Raúl Kripalani**: We can potentially create a pipeline for specs in a public calendar, allowing others to get involved.

**Whiteblock**: Do you want to open some Gitcoin grants or bounties to speed up the things?

**Mike Goelzer**:  We are open to making grants. If there are people who are interested in grant-work for improving the specs, they should get in touch with us.

**Danny Ryan**: I do want someone from each team to look at this PR to get merged relatively soon.
- [Libp2p Standardization Update #1281](https://github.com/ethereum/eth2.0-specs/pull/1281)


**Adrian Manning**: If people can look and give opinions, we can modify it.

**Jacek Sieka**: Do you anticipate we can use the same discovery for Eth1 and Eth2 at some point?

**Adrian Manning**: We're using DISC v5 at the moment.

**Danny Ryan**: If the question is "If Eth 1 is getting migrated to v5?" the answer is yes.

Discover v5, contacted people for an audit on the protocol.


#### 3.4.2 Gossiping Mechanism

**Timestamp: [1:07:56](https://youtu.be/YB8o_5qjNBc?t=4076)**

**Whiteblock**: Internal last week, we had Artemis, Prysmatic Labs, Lodestar for an exchange of handles using the Simple Hobbits approach.

Next step, improving the ability to Gossip bits between  different instances.

We're also trying create a testnet, which would create a test-bench (genesis event, peer recognition, exchange of block attestations, etc.).

One effort is to work on the gossiping approach. Right now our approach is very simple.

Another effort is creating utilities and tools for the community to run a testnet.


**Danny Ryan**: Some client are currently gossiping hashes and doing RPC calls for retrieval of that data. Our assumption is the latency will be too high and gossiping full objects is going to be the proper path.

**Whiteblock**: Right, we crippled this to a point where it's very very simple for the reason of just having interoperability.

At collection time you want to use something like Gossip Sub or even Episub.  All this needs to be benchmarked.

**Jonny Rhea**: At Preston's suggestion, we simplified the gossiping mechanism. Is that right Preston?

**Preston**: I think what you're referring to is when we're creating the announcement messages.

In terms of keeping it simple, I think that's for the Hobbit's implementation. It's to see basic interops.

**Danny Ryan**: Announcement of identifier and subsequent request, though it does same bandwidth, may induce excessive latencies on the network.

Potentially there's a hybrid strategy, but I don't the extreme of strictly gossiping identifier at the beginning is gonna be the proper way.

**Preston**: It's worth looking into, but I agree there's now a round trip if you're trying to get blocks out pretty quickly.

**Jonny Rhea**: Danny, your suggestion is very similar to Episub or Epidemic Broadcast Trees, just FYI that hybrid approach.

**Danny Ryan**: Jannik, what were your findings on the Episub experimentations?

**Jannik Luhn**: That it didn't have much, if at all.

Episub is different from what Danny just suggested because it's not based on timing.

**Jonny Rhea**: It's still a hybrid approach because you have the actual gossiping of the full block if it's an eager peer and if it's a lazy peer you just tell it, "Hey I have this". It splits the difference.

**Kevin Main-Hsuan Chia**: I think it's already in the Gossip Sub, that I want and I have this thing.

**Whiteblock**: Is it? Because I think Gossip Sub is probabilistic.

**Jonny Rhea**: Yeah, that was my understanding too.

**Whiteblock**: I don't know that Episub was implemented, since we have `libp2p` guys on the call, what's the level of maturity of Episub?

**Raúl Kripalani**: Episub was an idea in the pipeline, but not highly prioritized right now. Episub is optimal where you have very stable dissemination patterns in the network.  If we have a pattern of a small number of producers for Eth 2.0, then it'll be worth reactivating this discussion.

**Jonny Rhea**: I'd be interested if someone has looked into what's best for gossiping blocks as opposed to attestations if we've thought about that.

**Kevin Main-Hsuan Chia**: I want to add, I think the message identifier scheme is sorting process up now. Episub is more like you grab and prune the agents. It's a different scenario.

I think Jannik has done some pull-push simulation before?

**Jannik Luhn**: That was similar to Danny and such tested, but it also didn't happen. I don't remember why.

**Raúl Kripalani** Is there a reason you believe an Epidemic Broadcaster approach could be efficient for this message propagation paradigm that you have in Eth 2.0?

**Jonny Rhea**: I don't know. Maybe Episub is better for blocks and Gossip sub is better for attestations.

**Danny Ryan**: There might be a trade-off between what gossiping we're using for short subnets versus beacon subnet. I'm not certain.

**Raúl Kripalani**: If somebody could put together maybe a small blurb on what the difference is in message propagation on these particular circuits, then I can involve someone on the `libp2p` team who is a gossiping specialist. See if we could have a hybrid router to somehow arrive at different paths throughout the network.

**Danny Ryan**: I have some notes on this that describe the timing of the broadcast as well as the size and can add some notes about the stability of topics and stuff. I will pass it on to you.

**Jacek Sieka**: I'll point out, all these schemes introduce extra opportunities for failures and issues in general.

The minimum approach of gossiping full blocks is very very resilient. Full-proof so-to-speak.

Anything additional, we should be very careful of motivating that with substantial gains, because the simplicity of normal flooding makes it extremely resilient against all kinds of attacks.

**Whiteblock**: Whatever gossiping protocol we end up choosing we have this baseline where it's always possible to going back to flooding and it works.

We should have an adaptable approach where we start by flooding, and maybe optimize down the road. But we need to test that.

Did some testing of Flood Sub with Wedlock, it does not perform in the span of time with the number of bytes required for blocks, by the Eth 2.0 protocol. I might be wrong, I think there's more research and testing needed there.

**Jacek Sieka**: My understanding is, Gossip Sub was chosen for its substantial improvements in early experiments.

**Raúl Kripalani** Generally, it's all a matter of trade-offs.

Flood Sub is very resilient to all kinds of attacks as it's very naive.  However, it introduces a massive amplification factor on IO, which could potentially harm more than benefit. One trade-off.

Then as you start cutting down on the amplification factor, if a particular message arrives at a peer too many times due to the amplification factor, then you want to start getting more intelligent on how you tell a peer, "Stop sending me this message." Your trade-off here could be to reduce write amplification and overall traffic in the network.

Happy to continue the discussion.  Open to exploring different approaches.


### 3.5 [Spec Discussion](https://youtu.be/YB8o_5qjNBc?t=5095)

**Timestamp: [1:24:57](https://youtu.be/YB8o_5qjNBc?t=5095)**

**Danny Ryan**: I know implementers mentioned the SSE. There were a couple more escape types that were added to SSE.

This was done to:
1. Make the spec focus more on spec things and not low-level byte manipulation.
2. Provide a valuable set of types in SSE that might be used in other places, such as applications.

There are some issues there, so I want to open it up for a quick discussion, to fix the spec and move forward if we need to.

Dankrad, do you have anything to add?

**Dankrad Feist**: We want to understand pain-points. I think it's valuable to have in the SSE stack, but we don't want to make life hard for the implementers.

**Danny Ryan**: Is there still an open issue discussing this?

**Dankrad Feist**: I think the issue is closed at the moment. We can still re-open.

**Danny Ryan**: If there is discussion to be had, let's do this within the next 7 days in an issue. This is very critical for getting aligned with ConsenSys tests.

**Mamy Ratsimbazafy**: Just as a comment, the more types we have defined in the SSE spec the more efficient our code, at least in NIM, can be, in terms of both code size and performance.

**Danny Ryan**: Thanks. We have a few minutes left. Any questions left?

**Diederik Loerakker**: About SSE, where we can have, fixed-size, empty containers, and empty vectors. It's kinda troublesome.

Do we want to make empty vector illegal? Or do we want to make lists containing them illegal? Is there a use case for empty, fixed-size, containers?

**Vitalik Buterin**: We already made them illegal. We are revisiting that decision.

**Diederik Loerakker**: We made vectors illegal, but we also have containers. There's also inconsistency between lists being zero and vectors not being zero. I want to get this right and then we can move on.

**Dankrad Feist**: Before containers and empty vectors, they're both illegal. And now we added this new thing that lists can be of size zero. The question is, "Is it kinda weird that we forbid one thing and not the other?"

**Vitalik Buterin**: I'm okay forbidding, or not forbidding, lists with zero max length.

**Dankrad Feist**: The only question why you want to forbid it is because it might give us an easy way to "comment out" some features in the spec by setting some max lengths to zero.

**Diederik Loerakker**: We already discussed this issue. If any implemented would need this kind of type, please join the issue in the specs repository. Otherwise, I think it's not too important.

### 3.6 [Open Discussion/Closing Remarks](https://youtu.be/YB8o_5qjNBc?t=5540)

**Timestamp: [1:32:20](https://youtu.be/YB8o_5qjNBc)**

**Danny Ryan**: Any other things before we close today?

**Joseph Delong**: For the interop, I want to say the invitations went out to team leads. Those invitations are good until the 14th.

After that, we will reshuffle and send out more invitations to some of the teams that are wanting to attend. Please do register in the next 3 days.

**Danny Ryan**: It's easy and free to register.

We will likely meet in 2 weeks, you can take a look at the calendar first. Talk to everyone soon.
