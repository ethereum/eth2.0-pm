# Ethereum 2.0 Implementers Call 13 Notes

### Meeting Date/Time: Thursday 2019/2/28 at [14:00 GMT](https://savvytime.com/converter/gmt-to-germany-berlin-united-kingdom-london-ny-new-york-city-ca-san-francisco-china-shanghai-japan-tokyo-australia-sydney/feb-14-2019/2pm)
### Meeting Duration: 2 hours
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/31) 
### [Audio/Video of the meeting](https://youtu.be/0ZWG8hMbxes)

# Agenda
1. Testing Updates [_(3:00)_](https://youtu.be/0ZWG8hMbxes?t=181)
2. Client Updates
3. Research Updates
4. Phase 0 Wire Protocol
5. Serialization
6. Spec discussion
7. Open Discussion/Closing Remarks

# 1. Testing Updates
* _Notes: [3:00](https://youtu.be/0ZWG8hMbxes?t=181)_
  * Shared simplified fork choice test, abstract, not mentioning data structures. Most people seem to think this is better to reason about. Also shared ideas on state tests.  
  * Desire to have Prysmatics chain start tests in ETH 2.0 reference tests - Terence said he could add PR  
  * Whiteblocks is opensourcing testing and simulation  
  * BLS references tests are somewhat broken - serialization format is incorrect

# 2. Client Updates
* Pegasys - Steven [_(8:25)_](https://youtu.be/0ZWG8hMbxes?t=505)  
  * Upgrading to spec 0.4 
  * Have simulated blocks from a mock network adaptor executing state transition and fork choice rule
  * BLS largely working
  * Working to integrate other tools from Pegasys  
* PyEVM/Trinity - Hsiao-Wei Wang [_(9:29)_](https://youtu.be/0ZWG8hMbxes?t=569)  
  * On spec 0.4  
  * Testnet starting with devp2p network  
  * Working on python daemon libp2p binding  
* Prysmatic - Raul [_(10:40)_](https://youtu.be/0ZWG8hMbxes?t=640)  
  * On spec 0.4 aside from small bug fixes  
  * Working on simple testnet: 8 validators and beacon node  
  * Caution on working with committees at start of epoch. Lots of weird boundary conditions  
  * Adding cache layers  
  * Finished implementing initial sync of beacon node  
  * Working towards testnet  
* Nimbus - Mamy [_(12:22)_](https://youtu.be/0ZWG8hMbxes?t=742)  
  * Working towards testnet - primary missing piece is fork-choice
  * Targeting spec 0.3 to reduce impact of changes  
  * Full sync of initial beacon chain  
  * Progress on libp2p  
  * BLS in pipeline  
  * Presentation at ETHCC on tests and simulation to highlight tools for testnets  
* Lodestar - Greg [_(15:47)_](https://youtu.be/0ZWG8hMbxes?t=947)  
  * Done porting BLS from WASM  
  * Finished state transitions  
  * Aiming for simulations in the next week  
* Harmony - Mikhail [_(17:25)_](https://youtu.be/0ZWG8hMbxes?t=1045)  
  * Added support of configuration files, passing beacon chain parameters in YAML
  * Working towards 0.4 spec  
  * Merged OS license  
  * Stabilizing validator behavior  
* Parity - Wei Tang [_(19:13)_](https://youtu.be/0ZWG8hMbxes?t=1153)  
  * Launched simple testnets for CasperFFG, using to benchmark 
  * Updating to 0.4 spec - have committee shuffling, haven't integrated into state transition function  
* Yeeth - Dean [_(21:35)_](https://youtu.be/0ZWG8hMbxes?t=1295)
  * Updated to 0.4 - working on refactoring  
  * Trying libp2p headers in Swift  
  * BLS compiling properly, might use different library  
* Lighthouse - Adrian [_(22:26)_](https://youtu.be/0ZWG8hMbxes?t=1346)  
  * Cacheing committee info for processing blocks with 16,000 validators  
  * Building fork choice test framework and core network syncing and service infrastructure  
  * PR for Rust libp2p gossip sub implementation in progress  

* _Intros:_   
  * Mike Goelzer from Protocal Labs working on libp2p - just getting a pulse on ETH 2.0 development  
  * Matt Slipper from Kyokan - wrote Phase 0 wire protocol and the "State of ETH 2.0" report  

# 3. Research Updates  
* Justin Drake - [_(25:43)_](https://youtu.be/0ZWG8hMbxes?t=1543)  
  * Created meta issue "Misc Beacon State Changes" to keep track of remaining issues to change for Phase 0  
  * Possibly working towards executable spec vs human readable (current) - Submitted 10 ETH bounty, Protolambda is working on it in Go
  * Want to return to SHA256 design decision - many projects are moving towards SHA256, but there are security concerns  
  * Need standardization on hash functions for standardization on BLS - in context SHA256 would help with this  
  * Helpful to remember whatever we choose isn't absolutely permanent, it just needs to serve us well for the next several years  
  * Looking into SHA256 security - length extension attack & academic security reductions  
  * Recently discovered ETH 2.0 light clients might be more valuable than previously thought. Potentially DOS attack on fork choice rule that light clients could navigate.  
* Danny 31:45
  
  























